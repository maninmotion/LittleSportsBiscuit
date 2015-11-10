from django.core.management.base import BaseCommand, CommandError
from LittleSportsBiscuit.models import Team, Player, Roster

class Command(BaseCommand):
    help = "This is the help line"

    def handle(self, *args, **options):
        self.stdout.write("There are {} many Teams".format(Team.objects.count()))
