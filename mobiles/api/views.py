from rest_framework.views import APIView
from mobiles.models import Mobile
from .serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

class MobileAPIView(APIView):

    def get_permissions(self):
        if self.request.method =='POST':
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

    def get(self,request):
        queryset=Mobile.objects.all()
        serializer = MobileSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)