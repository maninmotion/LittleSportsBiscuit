from django.core.management.base import BaseCommand, CommandError
from LittleSportsBiscuit.models import Team, Player, Roster

class Command(BaseCommand):
    help = "This is the help line"

    def handle(self, *args, **options):
        #http://www.ourlads.com/ncaa-football-depth-charts/depth-chart/south-carolina/91832
        self.stdout.write("There are {} many Teams".format(Team.objects.count()))
