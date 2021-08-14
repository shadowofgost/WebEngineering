from django.db import models
from ..UserModel.Database import UserModel

class MmxModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             blank=True, primary_key=True)
    id_data = models.IntegerField(
        default=1, null=True, db_column='ID_Data', blank=True)
    id_type = models.SmallIntegerField(
        default=1, null=True, db_column='ID_Type', blank=True)
    ######id_type字段为媒体类型，1为PPT类型######
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models.ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='mmx_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmx'


class MmxDataModel(models.Model):
    id = models.OneToOneField(
        MmxModel, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID', related_name='mmxdata_related_to_mmx'
    )
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='mmxdata_related_to_user'
    )
    data = models.TextField(db_column='Data', blank=True)
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmxdata'
