from rest_framework.views import APIView
from mobiles.models import Mobile
from .serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

class MarketPlaceMobileAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            permission = [IsAuthenticated()]
        else:
            permission = [AllowAny()]
        return permission

    def get(self,request):
        queryset = Mobile.objects.all()
        serializer = MobileSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return response
