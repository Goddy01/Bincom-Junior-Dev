from django.shortcuts import render
from django.db import connection
from election.models import AnnouncedPuResults

# Create your views here.
def question1(request):
    polling_units = AnnouncedPuResults.objects.all()
    return render(request, 'question1.html', {'polling_units': polling_units})