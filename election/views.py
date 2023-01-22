from django.shortcuts import render
from django.db import connection
from election.models import AnnouncedPuResults, PollingUnit
import random

# Create your views here.
def question1(request):
    context = {}
    announced_pu_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=10)

    context['announced_pu_results'] = announced_pu_results
    # context['polling_unit_details'] = polling_unit_details
    return render(request, 'question1.html', context)