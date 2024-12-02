from django.urls import path
from mobile_marketplace.bids.api.views import BidPostAPIView, BidOnMobileGetAPIView

urlpatterns = [
    path("create_mobile-bid/", BidPostAPIView.as_view(), name="bid-amount"),
    path("get_all_bids-on-mobile/<int:pk>/", BidOnMobileGetAPIView.as_view(), name="bids-on-mobile")
]
