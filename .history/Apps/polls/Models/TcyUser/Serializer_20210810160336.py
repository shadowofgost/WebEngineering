from rest_framework.serializers import ModelSerializer
from .Database import UserModel, UserExtensionModel
class UserSerializer(ModelSerializer):
class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class Userex(ModelSerializer):
    class Meta:
        model = UserExtensionModel
        fields = '__all__'
