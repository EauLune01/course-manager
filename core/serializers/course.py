from rest_framework import serializers

from core.models import Course, Department, Professor
from core.serializers.department import DepartmentSerializer
from core.serializers.professor import ProfessorSerializer


class CourseSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(), write_only=True)
    department = DepartmentSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        professor_id = validated_data.pop('professor_id')
        course = Course.objects.create(department=department_id, professor=professor_id, **validated_data)
        return course