"""Platzigram views"""
import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse


def hello_world(request):
    '''Return a greeting'''

    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))
        )

def sorted(request):
    """Sorted."""
    numbers = request.GET['numbers']
    numbers = sorted([int(i) for i in numbers.split(',')])
    data = {
        'status' : 'ok',
        'numbers' : numbers,
        'message' : 'Numbers sorted succesfully'
    }
    #import pdb; pdb.set_trace()
    return JsonResponse(
        json.dumps(data), 
        content_type='application/json', 
        safe=False
        )

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {} you are not allowed here'.format(name)
    else:
        message = 'Hi {} welcome to platzigram'.format(name)
    
    return HttpResponse(message)