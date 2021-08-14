from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    Index,
    BigAutoField,
)
from ..UserModel.Database import UserModel


class TableInformationModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True,unique=True, blank=True)
    name = CharField(default="0", null=True, db_column="Name", max_length=50,blank=True)
    nametable = CharField(default="0", null=True, db_column="NameTable", max_length=50,blank=True)
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate",blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64,blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="kaoqin_related_to_user",
        db_constraint=False,
    )
    imark = SmallIntegerField(default=0, null=True, db_column="IMark",blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)
    back_up3 = IntegerField(default=0, null=True,blank=True)

    class Meta:
        db_table = "t_cytableinfo"
        indexes = [
            Index(fields=["id"],name="id_index"),
            Index(fields=["name"],name="name_index"),
            Index(fields=["nametable"],name="nametable_index"),
        ]
        ordering = ["id", "name"]
