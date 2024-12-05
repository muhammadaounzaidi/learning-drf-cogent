from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from mobile_marketplace.bids.api.v1.serializers import BidSerializer
from rest_framework.response import Response
from rest_framework import status
from mobile_marketplace.bids.models import Bid
from mobile_marketplace.mobiles.models import Mobile
from mobile_marketplace.bids.choices import BidStateTypes
from mobile_marketplace.bids.permissions import IsMobileOwner
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


class BidCreateAPIView(APIView):
    def post(self, request):
        serializer = BidSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MobileBidListAPIView(APIView):
    def get(self, request, pk):
        mobile = get_object_or_404(Mobile, id=pk)
        bids_on_mobile = Bid.objects.filter(mobile=mobile)
        serializer = BidSerializer(bids_on_mobile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BidAcceptAPIView(APIView):
    permission_classes = [IsMobileOwner]

    def get_object(self, pk):
        return get_object_or_404(Bid, pk=pk, state=BidStateTypes.PENDING)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = BidSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance.accept_bid()

        return Response(serializer.data, status=status.HTTP_200_OK)


# Generic Views


class BidCreateGenericAPIView(CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class MobileBidGenericListAPIView(ListAPIView):
    serializer_class = BidSerializer
    ordering_fields = ['amount']
    filterset_fields = ['state']

    def get_queryset(self):
        mobile = get_object_or_404(Mobile, id=self.kwargs['pk'])
        return Bid.objects.filter(mobile=mobile).select_related('mobile')


class BidAcceptGenericAPIView(UpdateAPIView):
    permission_classes = [IsMobileOwner]
    serializer_class = BidSerializer
    queryset = Bid.objects.filter(state=BidStateTypes.PENDING)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        instance.accept_bid()

        return Response(serializer.data, status=status.HTTP_200_OK)

