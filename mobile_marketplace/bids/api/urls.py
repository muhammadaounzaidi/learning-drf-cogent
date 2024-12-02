from django.urls import path
from mobile_marketplace.bids.api.views import BidCreateAPIView, MobileBidListAPIView

urlpatterns = [
    path("create/", BidCreateAPIView.as_view(), name="create_bid"),
    path("mobile/<int:pk>/", MobileBidListAPIView.as_view(), name="mobile_bids")
]
