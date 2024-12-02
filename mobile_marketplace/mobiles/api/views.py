from rest_framework.views import APIView
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.bids.models import Bid
from mobile_marketplace.mobiles.api.serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from mobile_marketplace.bids.choices import BidStateTypes

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
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


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


class IsMobileSoldAPIView(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(Mobile, pk=pk)
        except Mobile.DoesNotExist:
            raise NotFound(detail="Mobile not found.")

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = MobileSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        bid = Bid.objects.filter(mobile=pk).last()

        if bid and bid.amount:
            validated_data = serializer.validated_data
            validated_data['is_sold'] = True

            Bid.objects.filter(mobile=pk).exclude(id=bid.id).update(status=BidStateTypes.REJECTED)
            bid.status = BidStateTypes.ACCEPTED
            bid.save()

            serializer.save(**validated_data)
            response = Response(serializer.data)
        else:
            error_message = {
                'message': ["No bids on this mobile"]
            }
            response = Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        return response
