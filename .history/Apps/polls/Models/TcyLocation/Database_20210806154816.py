from django.db import models
from ..UserModel.Database import UserModel

class LocationModel(models.Model):
    id = models.IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_parent = models.IntegerField(default=1, null=True,
                                    db_column='ID_Parent', blank=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=1024, blank=True)
    idmanager = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='location_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cylocation'
