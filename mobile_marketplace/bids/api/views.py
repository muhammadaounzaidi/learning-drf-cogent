from decimal import Decimal
from rest_framework.views import APIView
from mobile_marketplace.bids.api.serializers import BidSerializer
from rest_framework.response import Response
from rest_framework import status
from mobile_marketplace.bids.models import Bid
from mobile_marketplace.mobiles.api.serializers import MobileIDSerializer
from mobile_marketplace.mobiles.models import Mobile
from django.shortcuts import get_object_or_404


class BidCreateAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        mobile = get_object_or_404(Mobile, id=data['mobile'])
        new_bid_amount = Decimal(data['amount'])

        last_bid = Bid.objects.filter(mobile=mobile).order_by('-created').first()
        min_bid = Decimal(mobile.asking_amount if last_bid is None else last_bid.amount)

        if new_bid_amount <= min_bid:
            return Response(
                {'amount': [f'Bid amount must be greater than {min_bid}.']},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BidSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MobileBidListAPIView(APIView):
    def get(self, request, pk):
        serializer = MobileIDSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)
        bids_on_mobile = Bid.objects.filter(mobile=pk)
        serializer = BidSerializer(bids_on_mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
