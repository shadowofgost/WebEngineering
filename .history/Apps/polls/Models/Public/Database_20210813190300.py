from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DateTimeField,
    TextField,
    IntegerField,
    BooleanField,
    ManyToManyField,
    OneToOneField,
    CASCADE,
    BigAutoField,
)
from ..UserModel.Database import UserModel

class BaseModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True, unique=True, blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    imark = IntegerField(default=0, null=True, db_column="IMark", blank=True)
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="plan_related_to_user",
        db_constraint=False,
    )
    back_up1 = CharField(default=0, null=True, max_length=254, blank=True)
    back_up2 = CharField(default=0, null=True, max_length=254, blank=True)
    back_up3 = IntegerField(default=0, blank=True, null=True)
    back_up4 = IntegerField(default=0, null=True, blank=True)
