from django.db import models

# Create your models here.

class Stadium(models.Model):
    """description"""
    stadium_id = models.AutoField(primary_key=True)
    stadium_name = models.CharField(max_length=100, null=True)
    capacity = models.PositiveIntegerField(null=True)
    guest_sector_capacity = models.PositiveIntegerField(null=True)
    year_of_construction = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return f"{self.stadium_name}"

class Club(models.Model):
    """description"""
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100, null=True)
    headquarter = models.CharField(max_length=100, null=True)
    website = models.URLField(max_length=200, null=True)
    president = models.CharField(max_length=150, null=True)
    coach = models.CharField(max_length=150, null=True)
    assistant_coach = models.CharField(max_length=150, null=True)
    stadium = models.ForeignKey(Stadium, null=True, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return f"{self.club_name}"

class Player(models.Model):
    """description"""
    player_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.surname}"

class Season(models.Model):
    """description"""
    season_id = models.AutoField(primary_key=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{str(self.start_date.year)}/{str(self.end_date.year)[2:]}"

class PlayerClubOfSeason(models.Model):
    """description"""
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name="seasonteam_set")
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL, related_name="seasonteam_set")
    season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL, related_name="seasonteam_set")



class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    matchday = models.PositiveIntegerField(null=True)
    referee = models.CharField(null=True, max_length=100)
    home_team = models.ForeignKey(Club, null=True, on_delete=models.CASCADE, related_name="home_matches")
    guest_team = models.ForeignKey(Club, null=True, on_delete=models.CASCADE, related_name="guest_matches")
    home_score = models.PositiveIntegerField(null=True)
    guest_score = models.PositiveIntegerField(null=True)
    season = models.ForeignKey(Season, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)


class MatchPlayer(models.Model):
    """Single match"""
    match_player_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
    
    pass


class MatchAction(models.Model):
    """description"""
    match_action = models.AutoField(primary_key=True)
    match_player = models.ForeignKey(MatchPlayer, null=True, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, null=True)
    minute = models.IntegerField(null=True)
    