from django.core.exceptions import SuspiciousOperation


class SuspiciousRequestPath(SuspiciousOperation):
    """Suspicious URL was requested."""

    pass
