from rest_framework.views import APIView
from .serializers import BidSerializer
from rest_framework.response import Response
from rest_framework import status
from bids.models import Bid


class BidPostAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BidSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response


class BidGetAPIView(APIView):
    def get(self, request, pk):
        bids_on_mobile = Bid.objects.filter(mobile=pk)
        serializer = BidSerializer(bids_on_mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
