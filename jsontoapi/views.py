from django.shortcuts import render

from .serializers import user1serializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def apisend(request):
    user1 = User1.objects.all()
    serializer = user1serializer(user1, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])

def apipost(request):
    serializer = user1serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# def apiform(request):
#     jsnodict = {'members':[]}
#     user1 = User1.objects.values()
#     for user in user1:
#         user['Activityperiods']=0
#         print(user)
#         jsnodict['members'].append(user)

class FormatList(APIView):
    def get(self,request):
        jsnodict = {'members':[]}
        user12 = User1.objects.values()
        for user in user12:
            print('u1',user)
            user13 = User1.objects.get(id = user['id'])
            activities = user13.activity_periods_set.values('start_time','end_time')
            print('act',activities)
            user['Activity_periods'] = []
            for activity in activities:
                user['Activity_periods'].append(activity) 
            jsnodict['members'].append(user)
        print(jsnodict['members'])

        return Response(jsnodict['members'],status = status.HTTP_202_ACCEPTED)