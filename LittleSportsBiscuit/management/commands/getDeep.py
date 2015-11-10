from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from urllib.request import urlopen
from LittleSportsBiscuit.models import Team, Player, Roster

class Command(BaseCommand):
    help = "This is the help line"

    def handle(self, *args, **options):
        thisUrl = "http://www.ourlads.com/ncaa-football-depth-charts/depth-chart/south-carolina/91832"
        thisCode = urlopen(thisUrl)
        thisObj = BeautifulSoup(thisCode, "html.parser")
        print(thisObj.title)
        self.stdout.write("There are {} many Teams".format(Team.objects.count()))
        #self.stdout.write(thisObj.title)
