from django.db import models


# Create your models here.
class Sport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Equipment(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    label = models.CharField(max_length=100)
    acquisition_date = models.DateField()

    def __str__(self):
        return self.label


class Venue(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT)
    length = models.FloatField()
    width = models.FloatField()

    @property
    def sport_label(self):
        return self.sport.label if self.sport else ""

    def __str__(self):
        return self.name


class TrainingRoom(models.Model):
    location = models.CharField(max_length=255)
    equipments = models.ManyToManyField(Equipment)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

    @property
    def venue_name(self):
        return self.venue.name if self.venue else ""

    @property
    def venue_sport(self):
        return self.venue.sport_label if self.venue else ""

    def __str__(self):
        return self.location


class Infrastructure(models.Model):
    SPORT_TYPE_CHOICES = (
        ('Foot', 'Football'),
        ('Rugby', 'Rugby'),
        ('Basket', 'Basketball'),
        ('Tennis', 'Tennis'),
        # Add other types de sports if necessary
    )

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=SPORT_TYPE_CHOICES)
    length = models.FloatField()
    width = models.FloatField()
    equipments = models.ManyToManyField(Equipment)

    @property
    def type_display(self):
        return self.get_type_display()

    def __str__(self):
        return self.name
