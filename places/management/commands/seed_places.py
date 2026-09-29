"""Load areas, categories, and places from data/places.csv."""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load areas, categories, and places from data/places.csv."

    def handle(self, *args, **options):
        raise NotImplementedError("Loading data/places.csv is not implemented yet.")
