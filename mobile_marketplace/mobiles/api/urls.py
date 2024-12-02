from django.urls import path
from mobile_marketplace.mobiles.api.views import (MobileListCreateAPIView,
                               MobileDetailAPIView,
                               UserMobileListAPIView,
                               IsMobileSoldAPIView)

urlpatterns = [
    path('marketplace/', MobileListCreateAPIView.as_view(), name='mobile-list-create'),
    path('marketplace/<int:pk>/', MobileDetailAPIView.as_view(), name='mobile-detail'),
    path("my-mobiles/", UserMobileListAPIView.as_view(), name="my_mobiles"),
    path("mobile-sold/<int:pk>/", IsMobileSoldAPIView.as_view(), name="is_mobile_sold"),
]
