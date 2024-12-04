from django.urls import path
from mobile_marketplace.bids.api.v1.views import (BidCreateAPIView, MobileBidListAPIView,
                                                  BidAcceptAPIView, BidCreateGenericView,
                                                  MobileBidGenericListView)

urlpatterns = [
    path('create/', BidCreateAPIView.as_view(), name='create_bid'),
    path('mobile/<int:pk>/', MobileBidListAPIView.as_view(), name='mobile_bids'),
    path('<int:pk>/accept/', BidAcceptAPIView.as_view(), name='accept_bid'),

    # Generic Views URL

    path('generic/create/', BidCreateGenericView.as_view(), name='create_bid'),
    path('generic/mobile/<int:pk>/', MobileBidGenericListView.as_view(), name='mobile_bids'),
]
