from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, BeaconSerializer
from .models import Beacon
from django.http import JsonResponse



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BeaconViewSet(viewsets.ModelViewSet):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


def send_json(request):
    data=[{'name':'arc','uuid':'12edc34fa66'},{'name':'arc2','uuid':'aefd3416fe43'}]
    return JsonResponse(data, safe=False)
