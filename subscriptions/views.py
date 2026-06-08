
from zoneinfo import ZoneInfo
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .services import CheckInService


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_in_view(request):

    try:
        visit = CheckInService.check_in(request.user)

        tashkent_time = visit.check_in_time.astimezone(
            ZoneInfo("Asia/Tashkent")
        )

        return Response({
            "status": "success",
            "message": "Kirish muvaffaqiyatli amalga oshirildi",
            "visit_id": visit.id,
            "check_in_time": tashkent_time.strftime("%Y-%m-%d %H:%M:%S")
        }, status=status.HTTP_200_OK)

    except ValueError as e:

        return Response({
            "status": "error",
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):

    active_sub = request.user.subscriptions.filter(
        status='active',
        end_date__gte=timezone.now()
    ).first()

    if active_sub:

        tashkent_end_date = active_sub.end_date.astimezone(
            ZoneInfo("Asia/Tashkent")
        )

        current_time = timezone.now().astimezone(
            ZoneInfo("Asia/Tashkent")
        )

        days_left = (
            tashkent_end_date.date() -
            current_time.date()
        ).days

        is_warning = days_left <= 3

    else:

        tashkent_end_date = None
        days_left = 0
        is_warning = False

    return Response({
        "phone": request.user.phone,
        "has_active_subscription": bool(active_sub),
        "active_plan": active_sub.plan.name if active_sub else None,
        "end_date": (
            tashkent_end_date.strftime("%Y-%m-%d %H:%M:%S")
            if tashkent_end_date else None
        ),
        "days_left": days_left,
        "is_warning": is_warning
    }, status=status.HTTP_200_OK)

