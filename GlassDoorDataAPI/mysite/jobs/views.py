from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd


def getJSON():
    data = pd.read_csv('..//glassdoor-scraper//src//output//output_02-10-2022.csv',encoding='cp1252' )
    data=data.to_json()
    return data


@api_view(['GET'])
def listjobs(request):
    Json_data = getJSON()
    # data = {'hello' :'user'}
    data = Json_data
    return Response(data)

def infoview(request):
    return render(request , 'jobs/infoview.html')

# # Create your views here.
# def listjobs(request):
#     return render(request , 'jobs/listview.html')