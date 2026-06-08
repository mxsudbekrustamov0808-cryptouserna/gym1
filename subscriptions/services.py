from django.utils import timezone
from .models import Subscription, VisitLog


class CheckInService:
    """
    Gym check-in logic
    """

    @staticmethod
    def check_in(user):

        active_subscription = Subscription.objects.filter(
            user=user,
            status='active',
            end_date__gte=timezone.now()
        ).order_by('-start_date').first()

        if not active_subscription:
            raise ValueError(
                "Faol obuna topilmadi yoki muddati tugagan!"
            )

        today_visits = VisitLog.objects.filter(
            subscription=active_subscription,
            check_in_time__date=timezone.now().date()
        ).count()

        if today_visits >= active_subscription.plan.max_visits_per_day:
            raise ValueError(
                f"Bugungi limit tugadi! Maksimal: "
                f"{active_subscription.plan.max_visits_per_day} ta"
            )

        visit = VisitLog.objects.create(
            user=user,
            subscription=active_subscription
        )

        return visit