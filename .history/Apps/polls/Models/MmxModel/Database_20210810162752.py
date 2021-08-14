from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    TextField,
    BigAutoField,
    Index,
)
from ..UserModel.Database import UserModel


class MmxModel(Model):
    id = BigAutoField(db_column="ID", blank=True, primary_key=True,unique=True)
    id_data = IntegerField(default=0, null=True, db_column="ID_Data", blank=True)
    """
    id_type_choices = [
            (1,"PPT")
        ]
    """
    """
    id_type = SmallIntegerField(default=1, null=True, db_column="ID_Type", blank=True,choices=id_type_choices)
    """
    id_type = SmallIntegerField(default=1, null=True, db_column="ID_Type", blank=True)
    ######id_type字段为媒体类型，1为PPT类型######
    timeupdate = IntegerField(default=1, null=True, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmx_related_to_user",
        db_constraint=False,
    )
    imark = SmallIntegerField(default=0, null=True, db_column="IMark",blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64,blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "t_cymmx"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_data"], name="id_data_index"),
            Index(fields=["id_type"], name="id_type_index"),
        ]
        ordering = ["id", "id_data","id_type"]


class MmxDataModel(Model):
    id = OneToOneField(
        MmxModel,
        to_field="id",
        on_delete=CASCADE,
        primary_key=True,
        db_column="ID",
        related_name="mmxdata_related_to_mmx",
        db_constraint=False,
    )
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmxdata_related_to_user",
        db_constraint=False,
    )
    data = TextField(db_column="Data", blank=True)
    imark = SmallIntegerField(default=0, null=True, db_column="IMark",blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "t_cymmxdata"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["timeupdate"], name="timeupdate_index"),
        ]
        ordering = ["id"]
