from rest_framework.serializers import ModelSerializer
from .Database import UserModel, UserExtensionModel
class UserModelSerializerShort(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class UserExtensionModelSerializer(ModelSerializer):
    class Meta:
        model = UserExtensionModel
        fields = '__all__'
