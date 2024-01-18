from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from account.serializers import PublicUserSerializer


class PublicUserRegistration(CreateAPIView):
    serializer_class = PublicUserSerializer
    permision_classes = [AllowAny]