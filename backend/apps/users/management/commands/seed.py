from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.users.factories import UserFactory
from apps.apartments.factories import ApartmentFactory

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        if User.objects.exists():
            self.stdout.write(self.style.WARNING('Seed skipped: Users already exist.'))
            return

        # Seed users
        users = UserFactory.create_batch(10)

        # Seed apartments
        for user in users:
            ApartmentFactory.create_batch(5, owner=user)

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))