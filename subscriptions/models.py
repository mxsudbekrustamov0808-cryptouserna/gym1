from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name="Obuna nomi")
    duration_days = models.PositiveIntegerField(verbose_name="Muddati (kun)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    max_visits_per_day = models.PositiveIntegerField(default=1, verbose_name="Kuniga max tashrif")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    def __str__(self):
        return f"{self.name} ({self.duration_days} kun)"


class Subscription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(MembershipPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timezone.timedelta(days=self.plan.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.plan.name}"


class VisitLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='visits')
    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.check_in_time.date()}"