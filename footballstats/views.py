from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


from .models import *

# Create your views here.


# for debug and development START
import inspect

def temporary_response_generator(method_name : str, request_title : str, response_body : str):
    response_str : str = f"""<html>
                                <p>method: {method_name}</p>
                                <h1>{request_title}</h1>
                                <p>{response_body}</p>
                            </html>"""
    return response_str

# for debug and development END

def teams(request):
    all_clubs = Club.objects.all()

    return render(request, "footballstats/teams.html", {
        "teams" : all_clubs #.capitalize()
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
    players = Player.objects.all()

    return render(request, "footballstats/players.html", {
        "players" : players
    })

def player(request, player_id):
    player = Player.objects.filter(player_id=player_id)

    return render(request, "footballstats/player.html", {
        "player" : player
    })

def matches(request):
    if request.method == "GET":
        season = "2023/24"
        matchday = 1
    else:
        data = request.POST
        season = data.get("season")
        matchday = data.get("matchday")
        print(f"season = {season}, matchday = {matchday}")


    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"All matches in current season"
    response_body : str = "List of all matches of current season."

    matches = Match.objects.all()
    seasons = SeasonPart.objects.filter(season_part=1)

    for s in seasons:
        print(f"season_id = {s.season_part_id}")

    matchdays = set([match.matchday for match in matches])

    return render(request, "footballstats/matches.html", {
        "matches" : matches,
        "seasons": seasons,
        "matchdays": matchdays,
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