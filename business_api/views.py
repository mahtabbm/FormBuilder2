from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

from business_api import permissions, serializers, models


class LoginApiView(APIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.Business.objects.all()

    def post(self, request):
        """create a new user"""
        serializer = self.serializer_class(data=request.data)


class RegisterViewSet(viewsets.ModelViewSet):
    """handle creating and updating a business user"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.Business.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.AccessOwnProfile,)

    http_method_names = ['post']

    """
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )
    """

    """
    def retrieve(self, request, pk=None):
        return Response(None)
    """


class LoginApiView(ObtainAuthToken):
    """handling creating business authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES







