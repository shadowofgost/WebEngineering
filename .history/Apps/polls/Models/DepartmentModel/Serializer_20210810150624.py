from rest_framework.serializers import ModelSerializer
from .Database import TcyDept
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model=TcyDept
        fields="__all__"
