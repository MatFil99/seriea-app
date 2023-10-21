from django.urls import path
from . import views

urlpatterns = [
    # /teams/
    path("teams/", views.teams, name="teams"),
    path("teams/<int:team_id>", views.team_by_id, name="team-base"),
    path("teams/<str:team>", views.team_by_name, name="team-base"),
    path("teams/<str:team>/players", views.team_players, name="team-players"),
    path("teams/<str:team>/matches", views.team_matches, name="team-matches"),

    # players
    path("players/", views.players, name="players"),
    path("players/<str:player>", views.player, name="player"),
    
    # matches
    path("matches/", views.matches, name="matches"),
    path("matches/str:season", views.matches_of_season, name="season-matches"),

    # statistics
    path("statistics/", views.statistics, name="statistics"),
]
