from django.shortcuts import render
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer,WorkspaceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Member,Workspace
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class MemberProfileView(ModelViewSet):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Member.objects.filter(user_id = self.request.user.id)



class WorkspaceView(ModelViewSet):
    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        (member_id,created) = Member.objects.get_or_create(user_id = self.request.user.id)
        return Workspace.objects.filter(members = member_id)



