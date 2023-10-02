from django.db import models

# Create your models here.

class Club(models.Model):
    """description"""
    club_name = models.CharField(max_length=100, null=True)
    headquarter = models.CharField(max_length=100, null=True)
    website = models.URLField(max_length=200, null=True)
    president = models.CharField(max_length=150, null=True)
    coach = models.CharField(max_length=150, null=True)
    assistant_coach = models.CharField(max_length=150, null=True)


    def __str__(self) -> str:
        return f"{self.club_name}"


class Stadium(models.Model):
    """description"""
    stadium_name = models.CharField(max_length=100, null=True)
    capacity = models.PositiveIntegerField(null=True)
    guest_sector_capacity = models.PositiveIntegerField(null=True)
    year_of_construction = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    # stadium_id = 
    def __str__(self) -> str:
        return f"{self.stadium_name}"

class Player(models.Model):
    """description"""
    firstname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.surname}"

class SeasonPart(models.Model):
    """description"""
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    season_part = models.CharField(max_length=1, null=True)

    def __str__(self) -> str:
        return f"{str(self.start_date.year)}/{str(self.end_date.year)[2:]}"

class Match(models.Model):
    """Single match"""
    # seasonpart_id = models.PositiveIntegerField(null=True)
    # home_team_id = 
    # guest_team_id = 
    
    pass

class MatchAction(models.Model):
    """description"""
    pass
    action = models.CharField(max_length=100, null=True)