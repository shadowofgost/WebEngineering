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


class TcyTypera(Model):
    id = BigAutoField(db_column="ID", blank=True, primary_key=True,unique=True)
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=128, blank=True
    )
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="typera_related_to_user",
        db_constraint=False,
    )
    imark = SmallIntegerField(default=0, null=True, db_column="IMark",blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64,blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "t_cytypera"
        indexes = [
            Index(fields=["id"], name="id_index"),
            Index(fields=["id_parent"],name="id_parent_index"),
            Index(fields=["name"], name="name_index"),
        ]
        ordering = ["id", "id_parent","name"]
