
from rest_framework import serializers
from .Database import UserModel, UserExtensionModel,DepartmentModel
class UserModelSerializer(serializers.ModelSerializer):
    department_name = serializers.SlugRelatedField(slug_field='name',source='deptid',queryset=DepartmentModel.objects.all())
    class Meta:
        model = UserModel
        field = '__all__'
        exclude = ("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")

class UserExtensionModelSerializerIn(serializers.ModelSerializer):
    nouser = serializers.SlugRelatedField(slug_field='nouser',source='id_user',queryset=UserModel.objects.all())
    idmanager_nouser = serializers.SlugRelatedField(slug_field='nouser',source='idmanager',queryset=UserModel.objects.all())
    class Meta:
        model = UserExtensionModel
        fields = '__all__'
        exclude =("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")

class UserExtensionModelSerializerOut(UserExtensionModelSerializerIn):
    name = serializers.SlugRelatedField(slug_field='name',source='id_user',queryset=UserModel.objects.all())
    idmanager_name = serializers.SlugRelatedField(slug_field='name',source = "idmanager",queryset=UserModel.objects.all())
    class Meta(UserExtensionModelSerializerIn.Meta):
        fields = '__all__'



class UserModelTotalSerializer(serializers.ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=UserModel.objects.all(), validators=[<UniqueValidator(queryset=UserExtensionModel.objects.all())>])
    photo = serializers.ModelField(model_field=<django.db.models.fields.BinaryField: photo>, read_only=True)
    timeupdate = serializers.IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    imark = serializers.IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    rem = serializers.CharField(allow_blank=True, allow_null=True, max_length=64, required=False)
    back_up1 = serializers.CharField(allow_blank=True, allow_null=True, max_length=254, required=False)
    back_up2 = serializers.IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    back_up3 = serializers.IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    idmanager = PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    def create(self,instance,validated_data):
        pass
