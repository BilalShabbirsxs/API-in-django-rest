from rest_framework import serializers
from .models import MonthlyStats


class MonthlyStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlyStats
        fields = ('url', 'id', 'revenue', 'cost', 'month')
