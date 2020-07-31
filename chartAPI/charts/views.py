from django.shortcuts import render
from rest_framework import viewsets
from .models import MonthlyStats
#from rest_framework import permissions
from .serializers import MonthlyStatsSerializer


class MonthlyStatsView(viewsets.ModelViewSet):
    queryset = MonthlyStats.objects.all()
    serializer_class = MonthlyStatsSerializer
    #permission_classes = [permissions.IsAuthenticated]
