from django.core.management.base import BaseCommand
from django.db import transaction

from account.services.users import UserService


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            user_service = UserService()

            super_user = user_service.create_superuser(
                email="imran@gmail.com",
                password1="123456",
                password2="123456",
                first_name="Imran",
                last_name="Potter",
            )
            self.stdout.write("Super user has been created.")