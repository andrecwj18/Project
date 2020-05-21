import os
import slack
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render # Added to render using template
from slack import WebClient
from slack.errors import SlackApiError

def index(request):

    now = datetime.now()

    client = slack.WebClient(token='xoxb-1117595367669-1112289286710-xTVNKvdVmIahi44jio9BPs3i')

    response = client.chat_postMessage(
        channel = 'D0146R9ABME',
        text = "Hello world!")

    assert response["ok"]
    assert response["message"]["text"] == "Hello world!"

    return render(request, "", {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d, %B, %Y at %X")
        })