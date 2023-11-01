from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from django.db.models import Q

import datetime as dt

from .models import *

import traceback


# Create your views here.


# for debug and development START
import inspect



# for debug and development END

def teams(request):
    if request.method == "GET":
        season = Season.objects.latest("start_date").season_id
    elif request.method == "POST":
        data = request.POST
        season = int(data.get("season"))

    club_ids = list(set([t.club.club_id for t in PlayerClubOfSeason.objects.filter(season=season)]))
    clubs = Club.objects.filter(club_id__in=club_ids)

    seasons = Season.objects.all()

    return render(request, "footballstats/teams.html", {
        "teams" : clubs,
        "seasons" : seasons,
        "season" : season,
    })

def team_by_id(request, team_id : int):
    # redirects to teams/CLUB_NAME
    try:
        selected_clubs = Club.objects.filter(club_id=team_id)
        club = selected_clubs[0] # get first club 
        return redirect("team-base", club.club_name)
    except:
        raise Http404()

def team_by_name(request, team : str):
    try:
        selected_clubs = Club.objects.filter(club_name=str.upper(team))
        club = selected_clubs[0] # get first club 
        return render(request, "footballstats/team.html", {
            "team" : club,
        })
    except:
        raise Http404()

def team_players(request, team : str):
    players = Player.objects.all()

    return render(request, "footballstats/players.html", {
        "players" : players
    })


def team_matches(request, team : str):
    matches = Match.objects.all()

    return render(request, "footballstats/matches.html", {
        "matches" : matches
    })


def players(request):
    if request.method == "GET":
        # get latest season
        season = Season.objects.latest("start_date").season_id
    
        club_ids = list(set([t.club.club_id for t in PlayerClubOfSeason.objects.filter(season=season)]))
        club = Club.objects.filter(club_id__in=club_ids).order_by("club_name")[0].club_id
    elif request.method == "POST":
        data = request.POST

        season_str = data.get("season")
        club_id_str = data.get("team") #Club.objects.filter(club_id__in=club_ids).order_by("club_name")[0]
        
        season = int(season_str) if season_str else None
        
        club_ids = list(set([t.club.club_id for t in PlayerClubOfSeason.objects.filter(season=season)]))

        if not club_id_str and season:
            # club = Club.objects.filter(club_id__in=club_ids).order_by("club_name")[0].club_id
            clubs_of_season = Club.objects.filter(club_id__in=club_ids).order_by("club_name")
            club_id = clubs_of_season[0] if clubs_of_season is not None else None
            club = club_id
        elif not club_id_str and not season:
            club_id = None
            club = club_id
        else:
            club_id = int(club_id_str)
            club = Club.objects.get(club_id=club_id).club_id

        # club = Club.objects.filter(club_id=club_id)[0].club_id
        
        # .club_id
        
    # get teams 
    clubs = Club.objects.filter(club_id__in=club_ids)
    # get players
    player_ids = list(set([p.player.player_id for p in PlayerClubOfSeason.objects.filter(season=season, club=club)]))
    players = Player.objects.filter(player_id__in=player_ids)

    seasons = Season.objects.all()

    print(f"club {club}")

    return render(request, "footballstats/players.html", {
        "players" : players,
        "seasons" : seasons,
        "teams" : clubs,
        "team" : club,
        "season" : season,
    })

def player(request, player_id):
    player = Player.objects.filter(player_id=player_id)

    return render(request, "footballstats/player.html", {
        "player" : player,
    })

def matches(request):
    if request.method == "GET":
        season = Season.objects.latest("start_date").season_id
        matchday = Match.objects.filter(season=season).latest("matchday").matchday

    else:
        data = request.POST

        season_str = data.get("season")
        matchday_str = data.get("matchday")
        
        season = int(season_str) if season_str else None
        if not matchday_str:
            matchday = Match.objects.filter(season=season).latest("matchday").matchday
        else:
            matchday = int(matchday_str) if matchday_str else None
        
    matches = Match.objects.filter(Q(season=season) & Q(matchday=matchday))
    matchdays = list(set([match.matchday for match in Match.objects.filter(season=season)]))

    seasons = Season.objects.all()

    print(f"season = {season}, matchday = {matchday}")

    return render(request, "footballstats/matches.html", {
        "matches" : matches,
        "seasons": seasons,
        "matchdays": matchdays,
        "matchday": matchday,
        "season" : season,
    })

def matches_of_season(request, season : str):

    matches = Match.objects.filter()

    return render(request, "footballstats/matches.html", {
        "matches" : matches
    })

def statistics(request):
    statistics = "statistics"

    return render(request, "footballstats/statistics.html", {
        "statistics": statistics
    })