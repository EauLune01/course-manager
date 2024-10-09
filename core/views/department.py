from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from core.models import Department
from core.serializers.department import DepartmentSerializer


class DepartmentListAPIView(APIView):
    def get_queryset(self):
        return Department.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetailAPIView(APIView):
    def get_queryset(self):
        return Department.objects.all()

    def get(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = DepartmentSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = DepartmentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)