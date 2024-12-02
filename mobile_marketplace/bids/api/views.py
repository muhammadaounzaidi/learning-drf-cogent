from rest_framework.views import APIView
from .serializers import BidSerializer
from rest_framework.response import Response
from rest_framework import status
from mobile_marketplace.bids.models import Bid


class BidPostAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BidSerializer(data=data)

        if serializer.is_valid():
            last_bid = Bid.objects.filter(mobile=data['mobile'], is_last_bid=True).first()
            new_bid_amount = int(data['amount'])

            if last_bid is None or new_bid_amount > last_bid.amount:
                bid = serializer.save()

                if last_bid:
                    last_bid.is_last_bid = False
                    last_bid.save()
                bid.is_last_bid = True
                bid.save()
                response = Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                error_message = {
                    'amount': [
                        f'Bid amount should be greater than the last bid of {last_bid.amount}'
                    ]
                }
                response = Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response


class BidOnMobileGetAPIView(APIView):
    def get(self, request, pk):
        bids_on_mobile = Bid.objects.filter(mobile=pk)
        serializer = BidSerializer(bids_on_mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
