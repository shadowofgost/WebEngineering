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
    def create(self,instance,validated_data):
        pass
    def update(self,instance,validated_data):
        pass
    def delete(self,instance,validated_data):
        pass
class UserExtensionModelSerializer(ModelSerializer):
    class Meta:
        model = UserExtensionModel
        fields = '__all__'
    def create(self,instance,validated_data):
        pass
    def update(self,instance,validated_data):
        pass
    def delete(self,instance,validated_data):
        pass
