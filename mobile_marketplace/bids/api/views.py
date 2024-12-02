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
        serializer = BidSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        new_bid_amount = Decimal(data['amount'])
        mobile_id = data['mobile']

        mobile = get_object_or_404(Mobile, id=mobile_id)
        asking_amount = Decimal(mobile.asking_amount)

        last_bid = Bid.objects.filter(mobile=mobile_id).order_by('-created').first()

        if last_bid is None:
            if new_bid_amount < asking_amount:
                error_message = {
                    'amount': [
                        f'Bid amount must be greater than the asking amount of {asking_amount}.'
                    ]
                }
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        if last_bid is None or new_bid_amount > last_bid.amount:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        error_message = {
            'amount': [
                f'Bid amount must be greater than the last bid of {last_bid.amount} '
            ]
        }
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class MobileBidListAPIView(APIView):
    def get(self, request, pk):
        serializer = MobileIDSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)
        bids_on_mobile = Bid.objects.filter(mobile=pk)
        serializer = BidSerializer(bids_on_mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
