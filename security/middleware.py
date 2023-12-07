import re
import logging
from django.conf import settings
from django.core.cache import cache
from .exceptions import SuspiciousRequestPath


class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.url_patterns = {
            "suspicious": [
                r"\.\.(/|\\)",
                r"etc/(group|shadow|passwd)",
                r"\.(pem|key|ssh)",
                r"\.(py|php|git)",
            ],
        }

        self.error_response_count_threshold = 15

        self.cache_config = {
            "prefix": "security",
            "duration_seconds": 60 * 5
        }

        self.logger = logging.getLogger("security")

    def __call__(self, request):
        client_ip = self.get_client_ip(request)

        self.check_suspicious_url_patterns(request)

        response = self.get_response(request)

        self.check_repeat_error_responses(request, response, client_ip)

        return response

    def get_client_ip(self, request):
        """Extracts the client's IP address from the given request's metadata."""

        if settings.USE_X_FORWARDED_HOST and ("HTTP_X_FORWARDED_FOR" in self.META):
            return self.META["HTTP_X_FORWARDED_FOR"]

        return request.META.get("REMOTE_ADDR", "")

    def build_cache_key(self, client_ip, key_suffix):
        return f"{self.cache_config.get('prefix')}:{client_ip}:{key_suffix}"

    def check_suspicious_url_patterns(self, request):
        for pattern in self.url_patterns.get("suspicious"):
            match = re.search(pattern, request.path)

            if match:
                raise SuspiciousRequestPath(f"Suspicious request path segment \"{match.group(0)}\"")

    def check_repeat_error_responses(self, request, response, client_ip):
        if 400 <= response.status_code < 600:
            cache_key = self.build_cache_key(client_ip, "repeat_error_responses")
            cache_timeout_seconds = self.cache_config.get("duration_seconds")

            exception_count = cache.get_or_set(key=cache_key, default=0, timeout=cache_timeout_seconds)
            cache.incr(cache_key)

            if exception_count == self.error_response_count_threshold:
                self.logger.error(f"Repeat error responses detected for client IP {client_ip}", extra={"request": request})
