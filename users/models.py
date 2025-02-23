import secrets
import string
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        blank=False,
        null=False,
        default=uuid.uuid4
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    ci = models.TextField(null=False, max_length=10, blank=False, unique=True)
    email = models.EmailField(
        null=False,
        unique=True,
        blank=False,
        max_length=45,
        db_index=True
    )
    token = models.TextField(
        max_length=10,
        editable=False,
        null=False,
        default=''
    )
    check_email = models.BooleanField(default=False, editable=False)
    username = models.CharField(
        max_length=15,
        blank=False,
        null=True,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.username

    def generate_token(self):
        new_token = string.ascii_letters + string.digits
        new_token = self.token = ''.join(
            secrets.choice(new_token) for _ in range(36))
        return new_token
