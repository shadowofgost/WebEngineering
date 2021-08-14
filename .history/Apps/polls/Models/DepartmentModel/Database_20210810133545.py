from django.db.models import (
    Model,
    CharField,
    IntegerField,
    SmallIntegerField,
    BigAutoField,
    Index
)

# Create your models here.


class TcyDept(Model):
    id = BigAutoField(db_column="ID", primary_key=True, unique=True, blank=True)
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=32, blank=True
    )
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    idmanager = IntegerField(default=0, null=True, db_column="IdManager", blank=True)
    imark = SmallIntegerField(default=0, null=True, db_column="IMark", blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    bakc_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "t_cydept"
        indexes = [
            Index(fields=["id_parent"], name="id_parent_index"),
            Index(fields=["id"], name="id_index"),
            Index(fields=["name"], name="name_index"),
        ]
        ordering = ["id", "name", "id_parent"]
