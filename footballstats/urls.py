from django.urls import path
from . import views

urlpatterns = [
    # /teams/
    path("teams/", views.teams, name="teams"),
    path("teams/<str:team>", views.team, name="team-base"),
    path("teams/<str:team>/players", views.team_players),
    path("teams/<str:team>/matches", views.team_matches),

    # players
    path("players/", views.players),
    path("players/<str:player>", views.player),
    
    # matches
    path("matches/", views.matches),
    path("matches/str:season", views.matches_of_season)
]
