from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.models import Course
from core.serializers.course import CourseSerializer


class CourseListAPIView(APIView):
    def get_queryset(self):
        return Course.objects.select_related("department", "professor").all()

    def get(self, request):
        qs = self.get_queryset()
        serializer = CourseSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    def get_queryset(self):
        return Course.objects.select_related("department", "professor").all()

    def get(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = CourseSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = CourseSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
