from rest_framework.views import APIView
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.mobiles.api.v1.serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.shortcuts import get_object_or_404
from mobile_marketplace.bids.permissions import IsMobileOwner


class MobileListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

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


class MobileDeleteAPIView(APIView):
    permission_classes = [IsMobileOwner]

    def delete(self, request, pk):
        mobile = get_object_or_404(Mobile, pk=pk)
        mobile.delete()
        return Response({"message": "Mobile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# Generic Views

class MobileListCreateGenericView(generics.ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class MobileGenericView(generics.RetrieveUpdateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class UserMobileGenericView(generics.ListAPIView):
    serializer_class = MobileSerializer

    def get_queryset(self):
        return Mobile.objects.filter(user=self.request.user)


class MobileDeleteGenericView(generics.DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
