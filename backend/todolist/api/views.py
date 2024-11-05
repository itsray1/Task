from django.shortcuts import render

# Create your views here.
import json
#from django.http import JsonResponse,HttpRequest 
from django.forms.models import model_to_dict

from tasks.models import Task

from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.serializers import TaskSerializer

# Create your views here.
@api_view(["Post"])
def api_home(request,*args,**kwargs):

   serializer=TaskSerializer(data=request.data)

   if serializer.is_valid(raise_exception=True):
      instance=serializer.save()
      print (instance)
      return Response(serializer.data)