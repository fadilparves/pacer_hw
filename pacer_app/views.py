from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random
from pacer_app.models import Score

def index(request):
    return HttpResponse("Hello, world. You're at the Pacer Homework Index.")

def get_score(request, user_id):
    # get the input from the request url
    input = request.GET.get('input')
    
    # generate random number between 1 to 100
    score = random.randint(1, 100) + int(input)

    # make sure the score is between 0 and 100
    if score >= 100:
        score = 100
    elif score <= 0:
        score = 0

    # create a new score object
    new_score = Score(score=score, user_id=user_id, username='test')

    # save the new score object
    new_score.save()

    # return the new score object as a json response with status code 200
    return JsonResponse({
        'user_id': new_score.user_id,
        'score': new_score.score,
        'date': new_score.date
    }, status=200)
     