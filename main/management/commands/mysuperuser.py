import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='geshin').exists():
            User.objects.create_superuser('geshin',
                                          'geshinaderemi06@myemail.com',
                                          'D06o09m15d22')