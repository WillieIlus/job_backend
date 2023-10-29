from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import JobSerializer, JobApplicationSerializer, ImpressionSerializer, ClickSerializer
from .models import Job, JobApplication, Impression, Click


class JobList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug'
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
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
    queryset = Impression.objects.all()
    serializer_class = ImpressionSerializer
    lookup_field = 'slug'

class ImpressionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Impression.objects.all()
    serializer_class = ImpressionSerializer
    lookup_field = 'slug'

class ClickList(ListCreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    lookup_field = 'slug'

class ClickDetail(RetrieveUpdateDestroyAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    lookup_field = 'slug'
    
