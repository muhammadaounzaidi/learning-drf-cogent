from rest_framework.views import APIView
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.bids.models import Bid
from mobile_marketplace.mobiles.api.serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


class MobileListCreateAPIView(APIView):
    def get_permissions(self):

        if self.request.method == 'POST':
            permission = [IsAuthenticated()]
        else:
            permission = [AllowAny()]
        return permission

    def get(self, request):
        queryset = Mobile.objects.all()
        serializer = MobileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = MobileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response


class MobileDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Mobile.objects.get(pk=pk)
        except Mobile.DoesNotExist:
            raise NotFound(detail="Mobile not found.")

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response


class UserMobileListAPIView(APIView):
    def get(self, request):
        queryset = Mobile.objects.filter(user=request.user)
        serializer = MobileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IsMobileSoldAPIView(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(Mobile, pk=pk)
        except Mobile.DoesNotExist:
            raise NotFound(detail="Mobile not found.")

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            bid = Bid.objects.filter(mobile=pk).last()
            validated_data = serializer.validated_data
            validated_data['is_sold'] = True

            if bid and bid.amount:
                validated_data['sold_amount'] = bid.amount
                serializer.save(**validated_data)
                response = Response(serializer.data)
            else:
                error_message = {
                    'message': [
                        "No bids on this mobile"
                    ]
                }
                response = Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response
