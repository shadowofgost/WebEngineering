from django.db.models import Model, CharField, ForeignKey, CASCADE,  IntegerField, ForeignKey, SmallIntegerField
from ..UserModel.Database import UserModel
class TableInformationModel(Model):
    id = IntegerField(default=1,  db_column='ID', primary_key=True)
    name = CharField(default='1', null=True,
                            db_column='Name', max_length=50)
    nametable = CharField(
        default='1', null=True,  db_column='NameTable', max_length=50)
    timeupdate = IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    idmanager =  ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='kaoqin_related_to_user'
    )
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    back_up1 = CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)
    back_up3 = IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cytableinfo'
