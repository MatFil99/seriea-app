from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


from .models import Club

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

    # method_name : str = inspect.stack()[0][3] + "()"
    # request_title : str = "List of all teams"
    # response_body : str = f"""There will be list of all teams. It will be possible to redirect to specific team page.
    # <br>{all_clubs_str}"""
    
    # temp_response = temporary_response_generator(method_name, request_title, response_body)
    # return HttpResponse(temp_response)

    return render(request, "footballstats/teams.html", {
        "teams" : all_clubs #.capitalize()
    })



def team(request, team : str):
    try:

        selected_clubs = Club.objects.filter(club_name=str.upper(team))

        # if not selected_clubs:
        #     return HttpResponseNotFound(f"Club {team} not found")

        club = selected_clubs[0] # get first club 

        # method_name : str = inspect.stack()[0][3] + "()"
        # request_title : str = f"Club general information - {team}"
        # response_body : str = "There will be general information about specific club. Clients can show matches, players of that team."

        # temp_response = temporary_response_generator(method_name, request_title, response_body)
        # return HttpResponse(temp_response)

        return render(request, "footballstats/team.html", {
            "team" : club,
        })
    except:
        raise Http404()

def team_players(requestm, team : str):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"Players of club - {team}"
    response_body : str = "View that will show players that are playing in certain club. Same basic information about them."

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)

def team_matches(request, team : str):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"Matches of club - {team}"
    response_body : str = "This site will list matches of specific club."

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)


def players(request):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"All players"
    response_body : str = "List of all players that was playing in Serie A league."

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)

def player(request, player):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"Player"
    response_body : str = "Information about player"

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)


def matches(request):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"All matches in current season"
    response_body : str = "List of all matches of current season."

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)

def matches_of_season(request, season : str):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"All matches in specific season"
    response_body : str = f"List of all matches of Serie A league in season {season}."

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)