from django.core.management.base import BaseCommand
from users.models import User
import os


class Command(BaseCommand):
    help = "Starts the app"

    def handle(self, *args, **options):
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        user = User()
        user.email = email
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()

        self.stdout.write(self.style.SUCCESS("Successfully created owner"))
