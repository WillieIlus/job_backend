from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import JobSerializer, JobApplicationSerializer, ImpressionSerializer, ClickSerializer
from .models import Job, JobApplication, Impression, Click
from .filters import JobFilter

class JobList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []



class JobDetail(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug'

class JobApplicationList(ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    lookup_field = 'slug'

class JobApplicationDetail(RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    lookup_field = 'slug'

class ImpressionList(ListCreateAPIView):
    # queryset = Impression.objects.all()
    serializer_class = ImpressionSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Impression.objects.filter(job_id=job_id)

class ImpressionDetail(RetrieveUpdateDestroyAPIView):
    # queryset = Impression.objects.all()
    serializer_class = ImpressionSerializer
    lookup_field = 'slug'

class ClickList(ListCreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Impression.objects.filter(job_id=job_id)

class ClickDetail(RetrieveUpdateDestroyAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    lookup_field = 'slug'
    
