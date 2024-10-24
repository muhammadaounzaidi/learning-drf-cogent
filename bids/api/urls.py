from django.urls import path
from bids.api.views import BidPostAPIView, BidGetAPIView

urlpatterns =[
    path("mobile-bid/", BidPostAPIView.as_view(), name = "bid-amount"),
    path("bids-on-mobile/<int:pk>/", BidGetAPIView.as_view(), name = "bids-on-mobile")
]
