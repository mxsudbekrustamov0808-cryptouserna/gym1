from django.contrib import admin
from .models import MembershipPlan, Subscription, VisitLog
from accounts.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'date_of_birth', 'is_active']
    search_fields = ['phone', 'username', 'email']
    list_filter = ['is_active']


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price', 'max_visits_per_day', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'plan']
    search_fields = ['user__phone', 'user__username']
    readonly_fields = ['start_date', 'end_date']


@admin.register(VisitLog)
class VisitLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription', 'check_in_time', 'check_out_time']
    list_filter = ['check_in_time']
    search_fields = ['user__phone']