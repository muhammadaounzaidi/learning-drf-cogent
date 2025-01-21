from django.urls import path
from mobile_marketplace.bids.api.v1.views import (BidCreateAPIView, MobileBidListAPIView,
                                                  BidAcceptAPIView, BidCreateGenericAPIView,
                                                  MobileBidGenericListAPIView, BidAcceptGenericAPIView)

urlpatterns = [
    path('create/', BidCreateAPIView.as_view(), name='create_bid'),
    path('mobile/<int:pk>/', MobileBidListAPIView.as_view(), name='mobile_bids'),
    path('<int:pk>/accept/', BidAcceptAPIView.as_view(), name='accept_bid'),

    # Generic Views URL

    path('generic/create/', BidCreateGenericAPIView.as_view(), name='create_bid_generic'),
    path('generic/mobile/<int:pk>/', MobileBidGenericListAPIView.as_view(), name='mobile_bids_generic'),
    path('generic/<int:pk>/accept/', BidAcceptGenericAPIView.as_view(), name='accept_bid_generic'),
]
