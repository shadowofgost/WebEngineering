from django.db.models import Model, CharField, ForeignKey, CASCADE,  IntegerField, ForeignKey, SmallIntegerField
from ..UserModel.Database import UserModel
class TyperaModel(Model):
    id = IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_parent = IntegerField(default=1, null=True,
                                    db_column='ID_Parent', blank=True)
    name = CharField(default='0', null=True,
                            db_column='Name', max_length=128, blank=True)
    timeupdate = IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager =  ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='typera_related_to_user'
    )
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cytypera'
