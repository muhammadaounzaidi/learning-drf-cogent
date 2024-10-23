from django.urls import path

from .views import MarketPlaceMobileAPIView

urlpatterns = [
    path("marketplace/", MarketPlaceMobileAPIView.as_view(), name="marketplace"),
]
