from django.db.models import Model, CharField, IntegerField, SmallIntegerField
# Create your models here.


class DepartmentModel(Model):
    id = IntegerField(default=1,  db_column='ID', primary_key=True)
    id_parent = IntegerField(
        default=1, null=True, db_column='ID_Parent')
    name = CharField(default='1', null=True,
                            db_column='Name', max_length=32)
    timeupdate = IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    idmanager = IntegerField(
        default=1, null=True, db_column='IdManager')
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    bakc_up1 = CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True,  blank=True)

    class Meta:
        db_table = 't_cydept'
