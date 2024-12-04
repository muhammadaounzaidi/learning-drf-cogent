from django.urls import path
from mobile_marketplace.mobiles.api.v1.views import (MobileListCreateAPIView,
                                                     MobileAPIView,
                                                     UserMobileListAPIView,
                                                     MobileDeleteAPIView,
                                                     MobileListCreateGenericView,
                                                     MobileGenericView,
                                                     UserMobileGenericView,
                                                     MobileDeleteGenericView)

urlpatterns = [
    path('', UserMobileListAPIView.as_view(), name='user_mobiles'),
    path('marketplace/', MobileListCreateAPIView.as_view(), name='marketplace'),
    path('<int:pk>/', MobileAPIView.as_view(), name='mobile_detail'),
    path('delete/<int:pk>/', MobileDeleteAPIView.as_view(), name='mobile-delete'),

    # Generic View URL

    path('generic/', UserMobileGenericView.as_view(), name='user_mobiles-generic'),
    path('generic/marketplace/', MobileListCreateGenericView.as_view(), name='marketplace-generic'),
    path('<int:pk>/generic/', MobileGenericView.as_view(), name='mobile_detail-generic'),
    path('generic/delete/<int:pk>/', MobileDeleteGenericView.as_view(), name='mobile-delete-generic'),
]
