from rest_framework.serializers import ModelSerializer
from .Database import UserModel, UserModelex
class UserSerializerShort(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class UserexSerializer(ModelSerializer):
    class Meta:
        model = UserModelex
        fields = '__all__'
