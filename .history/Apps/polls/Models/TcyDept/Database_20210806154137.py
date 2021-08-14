from django.db import models

# Create your models here.


class DepartmentModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    id_parent = models.IntegerField(
        default=1, null=True, db_column='ID_Parent')
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32)
    timeupdate = models.IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    idmanager = models.IntegerField(
        default=1, null=True, db_column='IdManager')
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    bakc_up1 = models.CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True,  blank=True)

    class Meta:
        db_table = 't_cydept'
