from rest_framework import viewsets, permissions
from .models import Course
from rest_framework.response import Response
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get (self, request, format=None):
        content= {
            'status':'request was permitted'
        }
        return Response(content)
    
    def put(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)