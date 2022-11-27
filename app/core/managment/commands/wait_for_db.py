"""
Django command to wait database to be avaible
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait database"""
    
    def handle(self, *args, **options):
        pass
    