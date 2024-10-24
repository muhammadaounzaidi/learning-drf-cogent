from django.urls import path

from .views import MobileListCreateAPIView, MobileDetailAPIView, UserMobileListAPIView

urlpatterns = [
    path('marketplace/', MobileListCreateAPIView.as_view(), name='mobile-list-create'),
    path('marketplace/<int:pk>/', MobileDetailAPIView.as_view(), name='mobile-detail'),
    path("my-mobiles/", UserMobileListAPIView.as_view(), name = "my_mobiles")
]
