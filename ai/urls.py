from django.urls import path
from .views import detect_traffic_sign, index

urlpatterns = [
    path("", index, name="index"),
    path("detect_traffic_sign/", detect_traffic_sign, name="detect_traffic_sign"),
]
