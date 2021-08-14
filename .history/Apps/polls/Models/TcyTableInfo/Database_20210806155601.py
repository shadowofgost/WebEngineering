from django.db import models
from ..UserModel.Database import UserModel
class TableInformationModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=50)
    nametable = models.CharField(
        default='1', null=True,  db_column='NameTable', max_length=50)
    timeupdate = models.IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    idmanager = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='kaoqin_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    back_up1 = models.CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cytableinfo'
