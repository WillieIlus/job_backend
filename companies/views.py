from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Company
from .serializers import CompanySerializer

class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'PUT':
            return [IsAuthenticated()]
        return []
    


class MyCompanyListAPIView(ListAPIView):
    serializer_class = CompanySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs  ):
        companies =  Company.objects.filter(user=self.request.user)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
