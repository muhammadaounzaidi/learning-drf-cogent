from django.urls import path
from mobile_marketplace.mobiles.api.v1.views import (MobileListCreateAPIView,
                                                     MobileAPIView,
                                                     UserMobileListAPIView,
                                                     MobileDeleteAPIView)

urlpatterns = [
    path('', UserMobileListAPIView.as_view(), name='user_mobiles'),
    path('marketplace/', MobileListCreateAPIView.as_view(), name='marketplace'),
    path('<int:pk>/', MobileAPIView.as_view(), name='mobile_detail'),
    path('delete/<int:pk>/', MobileDeleteAPIView.as_view(), name='mobile-delete')
]
