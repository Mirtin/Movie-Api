from django.contrib.auth.models import User

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class CurrentUserView(APIView):

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

def imagePage(request, image_title):
    image_data = open(f"accounts/user/avatar/{image_title}", "rb")

    return HttpResponse(image_data, content_type="image/png")

