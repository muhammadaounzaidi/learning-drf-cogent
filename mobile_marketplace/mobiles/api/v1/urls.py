from django.urls import path
from mobile_marketplace.mobiles.api.v1.views import (MobileListCreateAPIView,
                                                     MobileAPIView,
                                                     UserMobileListAPIView,
                                                     MobileDeleteAPIView,
                                                     MobileListCreateGenericAPIView,
                                                     MobileGenericAPIView,
                                                     UserMobileGenericAPIView,
                                                     MobileDeleteGenericAPIView)

urlpatterns = [
    path('', UserMobileListAPIView.as_view(), name='user_mobiles'),
    path('marketplace/', MobileListCreateAPIView.as_view(), name='marketplace'),
    path('<int:pk>/', MobileAPIView.as_view(), name='mobile_detail'),
    path('delete/<int:pk>/', MobileDeleteAPIView.as_view(), name='mobile_delete'),

    # Generic View URL

    path('generic/', UserMobileGenericAPIView.as_view(), name='user_mobiles_generic'),
    path('generic/marketplace/', MobileListCreateGenericAPIView.as_view(), name='marketplace_generic'),
    path('<int:pk>/generic/', MobileGenericAPIView.as_view(), name='mobile_detail_generic'),
    path('generic/delete/<int:pk>/', MobileDeleteGenericAPIView.as_view(), name='mobile-delete_generic'),
]
