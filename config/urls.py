from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mobile Bidding Platform",
        default_version='v1',
        description="API documentation for Mobile Bidding Platform",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('silk/', include('silk.urls', namespace='silk')),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('mobile_marketplace.users.api.v1.urls')),
    path('api/v1/mobiles/', include('mobile_marketplace.mobiles.api.v1.urls')),
    path('api/v1/bids/', include('mobile_marketplace.bids.api.v1.urls'))
]
