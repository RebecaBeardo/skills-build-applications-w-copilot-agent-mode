import os

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.reverse import reverse

from .views import (
    ActivityViewSet,
    LeaderboardEntryViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')


def api_root(request, format=None):
    return Response(
        {
            "base_url": base_url,
            "admin": reverse("admin:index", request=request, format=format),
            "teams": reverse("team-list", request=request, format=format),
            "users": reverse("user-list", request=request, format=format),
            "activities": reverse("activity-list", request=request, format=format),
            "leaderboard": reverse("leaderboard-list", request=request, format=format),
            "workouts": reverse("workout-list", request=request, format=format),
        }
    )

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/')),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
