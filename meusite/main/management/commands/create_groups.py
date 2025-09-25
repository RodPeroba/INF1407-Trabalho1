from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    def handle(self, *args, **options):
        Group.objects.get_or_create(name='Comprador')
        Group.objects.get_or_create(name='Vendedor')
        self.stdout.write('Grupos criados com sucesso!')
