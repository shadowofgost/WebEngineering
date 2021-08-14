
from rest_framework.serializers import ModelSerializer,CharField,IntegerField,ModelField,SlugRelatedField,ValidationError
from .Database import UserModel, UserExtensionModel
class UserModelSerializer(ModelSerializer):
    department_name = SlugRelatedField(slug_field='name',queryset=UserExtensionModel.objects.all(),source='deptid')
    class Meta:
        model = UserModel
        field = '__all__'
        exclude = ("back_up1","back_up2","back_up3")
    def create(self,validated_data):

    def update(self,validated_data):
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

class TotalSerializer(UserModelSerializer,UserExtensionModelSerializer):
    id = PrimaryKeyRelatedField(queryset=UserModel.objects.all(), validators=[<UniqueValidator(queryset=UserExtensionModel.objects.all())>])
    photo = ModelField(model_field=<django.db.models.fields.BinaryField: photo>, read_only=True)
    timeupdate = IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    imark = IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    rem = CharField(allow_blank=True, allow_null=True, max_length=64, required=False)
    back_up1 = CharField(allow_blank=True, allow_null=True, max_length=254, required=False)
    back_up2 = IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    back_up3 = IntegerField(allow_null=True, max_value=2147483647, min_value=-2147483648, required=False)
    idmanager = PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    def create(self,instance,validated_data):
        pass