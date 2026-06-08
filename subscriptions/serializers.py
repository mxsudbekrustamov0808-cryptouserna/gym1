from rest_framework import serializers
from .models import MembershipPlan, Subscription, VisitLog

class MembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipPlan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['end_date']

class VisitLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitLog
        fields = '__all__'