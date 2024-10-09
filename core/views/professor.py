from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.models import Professor
from core.serializers.professor import ProfessorSerializer


class ProfessorListAPIView(APIView):
    def get_queryset(self):
        return Professor.objects.select_related("department").all()

    def get(self, request):
        qs = self.get_queryset()
        serializer = ProfessorSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorDetailAPIView(APIView):
    def get_queryset(self):
        return Professor.objects.select_related("department").all()

    def get(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = ProfessorSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = ProfessorSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
