from django.urls import path

from .views import MobileAPIView

urlpatterns = [
    path("mobile/",MobileAPIView.as_view(),name="mobile"),
]
