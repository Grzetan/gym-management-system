from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        OWNER = "owner", _("owner")
        TRAINER = "trainer", _("trainer")
        EMPLOYEE = "employee", _("employee")
        CUSTOMER = "customer", _("customer")

    role = models.CharField(
        max_length=20, choices=Role.choices, null=False, default=Role.CUSTOMER
    )
    username = None
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
