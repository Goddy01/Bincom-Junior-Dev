from django.shortcuts import render
from django.db import connection
from election.models import AnnouncedPuResults, PollingUnit

# Create your views here.
def question1(request):
    announced_pu_results = AnnouncedPuResults.objects.all()
    return render(request, 'question1.html', {'announced_pu_results': announced_pu_results})