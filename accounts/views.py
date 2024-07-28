from django.contrib.auth.models import User
from .models import ProfileModel
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

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



class ChangeAvatarView(APIView):
    parser_classes = [MultiPartParser]

    def put(self, request, format=None):
        if 'file' not in request.data:
            return Response({"error": "Missing file parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.data['file']
        user = request.user

        profile, created = ProfileModel.objects.get_or_create(user=user)
        profile.avatar = file
        profile.save()
        response = {
                'msg': "Avatar updated" if not created else "Avatar created"
            }
        return Response(response, status=status.HTTP_200_OK)