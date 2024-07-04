from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from principal.models import Cliente  # Asegúrate de importar tu modelo Cliente

class Command(BaseCommand):
    help = 'Create Cliente for users without Cliente'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(cliente__isnull=True)
        for user in users:
            Cliente.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Cliente created for user {user.username}'))
