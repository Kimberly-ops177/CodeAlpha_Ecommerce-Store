from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Make a user a staff member and superuser'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to make staff')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()

            self.stdout.write(self.style.SUCCESS(
                f'Successfully made {username} a staff member and superuser!'
            ))
            self.stdout.write(self.style.SUCCESS(
                f'You can now log in to the admin panel at http://127.0.0.1:8000/admin/'
            ))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User {username} does not exist'))
