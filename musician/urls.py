from django.urls import path, include
from rest_framework import routers
from musician.views import MusicianViewSet


router = routers.DefaultRouter()
router.register("manage", MusicianViewSet, basename="manage")
urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
