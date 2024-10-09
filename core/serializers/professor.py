from rest_framework import serializers

from core.models import Professor, Department
from core.serializers.department import DepartmentSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)

    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        professor = Professor.objects.create(department=department_id, **validated_data)
        return professor
