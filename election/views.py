from django.shortcuts import render
from django.db import connection
# from bincom

# Create your views here.

# print('RE: ', polling_unit.objects.using('other').all())
def ye(request, filename):
    # def get_rows(filename):
    with open(filename, 'r') as f:
        sql = f.read()

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return row
    return render(request, 'question1.html')