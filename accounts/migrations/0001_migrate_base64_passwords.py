import base64

from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.db import migrations


def forwards_func(apps, _schema_editor):
    User = apps.get_model("auth", "User")

    hasher = PBKDF2PasswordHasher()
    users = User.objects.filter(password__startswith="base64$")

    for user in users:
        _algorithm, base64_string = user.password.split("$", 1)

        encoded_bytes = base64_string.encode("utf-8")
        password_bytes = base64.b64decode(encoded_bytes)
        password_string = password_bytes.decode("utf-8")

        salt = hasher.salt()
        password_pbkdf2 = hasher.encode(password_string, salt)

        user.password = password_pbkdf2
        user.save(update_fields=["password"])


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
