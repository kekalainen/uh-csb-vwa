import base64

from django.contrib.auth.hashers import BasePasswordHasher


class Base64PasswordHasher(BasePasswordHasher):
    """
    An insecure password "hasher".

    Stores passwords in Base64, prefixed with "base64$".
    """

    algorithm = "base64"

    def verify(self, password, encoded):
        return encoded == self.encode(password, None)

    def encode(self, password_string, _salt):
        password_bytes = password_string.encode("utf-8")
        encoded_bytes = base64.b64encode(password_bytes)
        encoded_string = encoded_bytes.decode("utf-8")

        return "%s$%s" % (self.algorithm, encoded_string)

    def decode(self, encoded):
        algorithm, hash = encoded.split("$", 1)

        return {
            "algorithm": algorithm,
            "hash": hash,
            "salt": None,
        }

    def safe_summary(self, encoded):
        return self.decode(encoded)

    def harden_runtime(self, _password, _encoded):
        pass
