from rest_framework.views import APIView
from mobiles.models import Mobile
from mobiles.api.serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound


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
        serializer = MobileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response


class MobileDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated()]

    def get(self, request):
        queryset = Mobile.objects.filter(user=request.user)
        serializer = MobileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
