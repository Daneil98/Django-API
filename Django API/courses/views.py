from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response



class CourseListView(generics.ListAPIView):
    course = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
    course = Course.objects.all()
    serializer_class = CourseSerializer
