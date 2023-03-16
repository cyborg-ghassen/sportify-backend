from django.db import models

from account.models import ClubUser
from structure.models import Infrastructure, Sport
from team.models import Team


# Create your models here.
class Match(models.Model):
    code = models.CharField(max_length=10, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1_set")
    opponent = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2_set")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.PROTECT)
    players = models.ManyToManyField(ClubUser, through='Participation')
    score = models.CharField(max_length=10)

    @property
    def team_name(self):
        return self.team.name if self.team else ""

    @property
    def opponent_name(self):
        return self.opponent.name if self.opponent else ""

    @property
    def infrastructure_name(self):
        return self.infrastructure.name if self.infrastructure else ""

    def __str__(self):
        return self.code


class Participation(models.Model):
    PLAYER_ROLES = [
        ('GK', 'Gardien de but'),
        ('DF', 'Défenseur'),
        ('MD', 'Milieu de terrain'),
        ('FW', 'Attaquant'),
    ]
    player = models.ForeignKey(ClubUser, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    jersey_number = models.PositiveSmallIntegerField()
    role = models.CharField(max_length=2, choices=PLAYER_ROLES)
    points = models.PositiveSmallIntegerField(default=0)
    fouls = models.PositiveSmallIntegerField(default=0)

    @property
    def player_nickname(self):
        return self.player.username if self.player else ""

    @property
    def player_fullname(self):
        return f"{self.player.first_name} {self.player.last_name}" if self.player else ""

    @property
    def match_code(self):
        return self.match.code if self.match else ""

    @property
    def role_display(self):
        return self.get_role_display()

    def __str__(self):
        return self.player.username


class TrainingSession(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    facility = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    @property
    def team_name(self):
        return self.team.name if self.team else ""

    @property
    def sport_name(self):
        return self.sport.label if self.sport else ""

    @property
    def facility_name(self):
        return self.facility.name if self.facility else ""

    def __str__(self):
        return f"{self.team} - {self.sport} - {self.facility}"

