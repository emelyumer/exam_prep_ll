from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from djangoProject.profiles.validator import validate_username


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )