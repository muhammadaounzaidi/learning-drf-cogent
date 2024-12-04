from rest_framework.views import APIView
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.mobiles.api.v1.serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class MobileListCreateAPIView(APIView):
    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method is 'GET':
            permissions.append(AllowAny())
        return permissions

    def get(self, request):
        queryset = Mobile.objects.all()
        serializer = MobileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MobileAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Mobile, pk=pk)

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserMobileListAPIView(APIView):
    def get(self, request):
        queryset = Mobile.objects.filter(user=request.user)
        serializer = MobileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
