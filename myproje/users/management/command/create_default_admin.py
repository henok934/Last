from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import Admin

class Command(BaseCommand):
    help = 'Create a default admin user'

    def handle(self, *args, **kwargs):
        default_username = 'admin'
        default_password = 'admin123'  # Change for security
        default_email = 'admin@example.com'
        default_phone = '1234567890'
        default_fname = 'Default'
        default_lname = 'Admin'
        default_gender = 'Other'

        if not Admin.objects.filter(username=default_username).exists():
            Admin.objects.create(
                username=default_username,
                password=make_password(default_password),
                email=default_email,
                phone=default_phone,
                fname=default_fname,
                lname=default_lname,
                gender=default_gender,
            )
            self.stdout.write(self.style.SUCCESS('Successfully created default admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
