from django.db import models

# Create your models here.

# Enum Choices Below
MFB = 'MFB'
SPORTS_CHOICES = (
    (MFB, 'Football'),
)

HC = 'HC'
OC = 'OC'
DC = 'DC'
TE = 'TE'
RB = 'RB'
OL = 'OL'
WR = 'WR'
DE = 'DE'
DB = 'DB'
DT = 'DT'
ST = 'ST'

COACHING_CHOICES = (
    (HC, 'Head Coach'),
    (OC, 'Off Coor'),
    (DC, 'Def Coor'),
    (TE, 'TE'),
    (RB, 'RB'),
    (OL, 'OL'),
    (WR, 'WR'),
    (DE, 'DE'),
    (DB, 'DB'),
    (DT, 'DT'),
    (ST, 'ST'),
)

FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
YEAR_IN_SCHOOL_CHOICES = (
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
)

QB = 'QB'
TB = 'TB'
FB = 'FB'
RT = 'RT'
RG = 'RG'
CE = 'CE'
LG = 'LG'
LT = 'LT'
TE = 'TE'
SE = 'SE'
FL = 'FL'
DE = 'DE'
DT = 'DT'
LB = 'LB'
CB = 'CB'
FS = 'FS'
SS = 'SS'
RB = 'RB'
PK = 'PK'
OL = 'OL'
WR = 'WR'
OG = 'OG'
NG = 'NG'
PT = 'PT'

PLAYER_CHOICES = (
    (QB, 'Quarterback'),
    (TB, 'Tail Back'),
    (FB, 'Full Back'),
    (RT, 'Right Tackle'),
    (RG, 'Right Guard'),
    (CE, 'Center'),
    (LG, 'Left Guard'),
    (LT, 'Left Tackle'),
    (TE, 'Tight End'),
    (SE, 'SE'),
    (FL, 'FL'),
    (DE, 'Defensive End'),
    (DT, 'Defensive Tackle'),
    (LB, 'Linebacker'),
    (CB, 'Corner Back'),
    (FS, 'Free Safety'),
    (SS, 'Strong Safety'),
    (RB, 'Running Back'),
    (PK, 'Place Kicker'),
    (OL, 'Offensive Line'),
    (WR, 'Wide Receiver'),
    (OG, 'Offensive Guard'),
    (NG, 'Nose Guard'),
    (PT, 'Punter'),
)

NA = 'NA'
REG = 'FN'
OT1 = 'OT1'
OT2 = 'OT2'
OT3 = 'OT3'
OT4 = 'OT4'
OTX = 'OTX'

FINAL_CHOICES = (
    (NA, 'NA'),
    (REG, 'Final'),
    (OT1, 'OT'),
    (OT2, 'OT2'),
    (OT3, 'OT3'),
    (OT4, 'OT4'),
    (OTX, 'OTX'),
)

class Conference(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
      return self.name


class Team(models.Model):
    name = models.CharField(max_length=75)
    conference = models.ForeignKey('Conference', related_name='conference')
    nickname = models.CharField(max_length=75)
    mascot = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=3,
                            choices=SPORTS_CHOICES,
                            default=MFB)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=75)
    sport = models.ForeignKey('Sport', related_name='coach_sport')
    team = models.ForeignKey('Team', related_name='coach_team')
    position = models.CharField(max_length=2,
                                choices=COACHING_CHOICES,
                                default=HC)
    previous = models.CharField(max_length=175, name='Previous Job')

    class Meta:
        verbose_name_plural = "Coaches"
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=75)
    height = models.FloatField(default=0)
    weight = models.IntegerField(default=0)
    jersey = models.IntegerField(default=0)
    highschool = models.CharField(max_length=100, blank=True)
    hometown = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=75, blank=True)
    school_class = models.CharField(max_length=2,
                                    choices=YEAR_IN_SCHOOL_CHOICES,
                                    default=FRESHMAN)

    def __str__(self):
        return self.name


class Roster(models.Model):
    year = models.IntegerField()
    sport = models.ForeignKey('Sport', related_name='roster_sport')
    team = models.ForeignKey('Team', related_name='roster_team')
    player = models.ForeignKey('Player', related_name='roster_player')
    position = models.CharField(max_length=2,
                                choices=PLAYER_CHOICES,
                                default=QB)
    #school_class = models.CharField(max_length=2,
    #                            choices=YEAR_IN_SCHOOL_CHOICES,
    #                            default=FRESHMAN)
    starter = models.BooleanField(default=1)
    redshirt = models.BooleanField(default=0)

    def __str__(self):
        return '{year} - {team} - {player} - {position}'.format(
            year=self.year, team=self.team.nickname, player=self.player, position=self.position)

    def is_starter(self):
        return bool(self.starter)


class Schedule(models.Model):
    date = models.DateTimeField()
    home_team = models.ForeignKey('Team', related_name='schedule_home_team')
    away_team = models.ForeignKey('Team', related_name='schedule_away_team')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    game_end = models.CharField(max_length=10,
                                choices=FINAL_CHOICES,
                                default=NA)

