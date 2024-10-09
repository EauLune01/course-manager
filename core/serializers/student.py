from rest_framework import serializers
from core.models import Student, Department
from core.serializers.department import DepartmentSerializer


class StudentSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        student = Student.objects.create(department=department_id, **validated_data)
        return student
