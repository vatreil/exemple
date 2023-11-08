import os

import requests
from django.shortcuts import render


def user(request, user_name):
    #DNS FOR REQUEST CONTROLEUR -> server_name
    try:
        print("http://" + str(os.getenv('URL_BACKEND')) + "/user/?user_name=" + user_name)
        response = requests.request("GET", "http://" + os.getenv('URL_BACKEND') + "/user/?user_name=" + user_name)
        body = response.json()
        return render(request, "index.html", context=body)
    except Exception as e:
        print(e)
        return render(request, "index.html")