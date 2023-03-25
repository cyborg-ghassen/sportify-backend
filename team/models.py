from django.db import models

from accounts.models import ClubUser


# Create your models here.
class Team(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    creation_date = models.DateField()
    colors = models.CharField(max_length=100)
    members = models.ManyToManyField(ClubUser, through='TeamMembership')

    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(ClubUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    @property
    def team_name(self):
        return self.team.name if self.team else ""

    @property
    def member_nickname(self):
        return self.member.username if self.member else ""

    @property
    def member_fullname(self):
        return f"{self.member.first_name} {self.member.last_name}" if self.member else ""

    def __str__(self):
        return self.team.name + " membership"
