from django.shortcuts import render
from django.http import HttpResponse


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


# Create your views here.


def home(request):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"Seriea home page"
    response_body : str = ""

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)


def about(request):
    method_name : str = inspect.stack()[0][3] + "()"
    request_title : str = f"Seriea about page"
    response_body : str = ""

    temp_response = temporary_response_generator(method_name, request_title, response_body)
    return HttpResponse(temp_response)
