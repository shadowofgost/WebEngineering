from django.db.models import Model, CharField, ForeignKey, CASCADE,  IntegerField, ForeignKey, SmallIntegerField,OneToOneField,TextField
from ..UserModel.Database import UserModel

class MmxModel(Model):
    id = IntegerField(default=1,  db_column='ID',
                             blank=True, primary_key=True)
    id_data = IntegerField(
        default=1, null=True, db_column='ID_Data', blank=True)
    id_type = SmallIntegerField(
        default=1, null=True, db_column='ID_Type', blank=True)
    ######id_type字段为媒体类型，1为PPT类型######
    timeupdate = IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='mmx_related_to_user'
    )
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmx'


class MmxDataModel(Model):
    id = OneToOneField(
        MmxModel, to_field="id", on_delete=CASCADE, primary_key=True, db_column='ID', related_name='mmxdata_related_to_mmx'
    )
    timeupdate = IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager =  ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='mmxdata_related_to_user'
    )
    data = TextField(db_column='Data', blank=True)
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmxdata'
