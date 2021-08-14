from ast import Index
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    BigAutoField,
)
from ..UserModel.Database import UserModel
from ..CurriculaModel.Database import CurriculaModel
from ..LocationModel.Database import LocationModel


class CoursePlanModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True, blank=True,unique=True)
    id_curricula = ForeignKey(
        CurriculaModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Curricula",
        related_name="id_curricula",
        db_constraint=False,
    )
    timebegin = IntegerField(default=0, null=True, db_column="TimeBegin", blank=True)
    timeend = IntegerField(default=0, null=True, db_column="TimeEnd", blank=True)
    id_location = ForeignKey(
        LocationModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Location",
        related_name="plan_related_to_location",
        db_constraint = False,
    )
    id_speaker = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_Speaker",
        related_name="plan_related_to_user_speaker",
        db_constraint=False,
    )
    attr = SmallIntegerField(default=0, db_column="Attr", blank=True)
    charge = SmallIntegerField(default=0, db_column="Charge", blank=True)
    pwaccess = SmallIntegerField(default=0, db_column="PwAccess", blank=True)
    pwcontinuous = SmallIntegerField(
        default=0, db_column="PwContinuous", blank=True
    )
    pwdirection = SmallIntegerField(
        default=0, db_column="PwDirection", blank=True
    )
    dooropen = SmallIntegerField(default=0, db_column="DoorOpen", blank=True)
    timebegincheckbegin = IntegerField(
        default=0, db_column="TimeBeginCheckBegin", blank=True
    )
    timebegincheckend = IntegerField(
        default=0, db_column="imeBeginCheckEnd", blank=True
    )
    timeendcheckbegin = IntegerField(
        default=0, db_column="TimeEndCheckBegin", blank=True
    )
    timeendcheckend = IntegerField(
        default=0, db_column="TimeEndCheckEnd", blank=True
    )
    rangeusers = CharField(
        default=0, null=True, db_column="RangeUsers", max_length=1024, blank=True
    )
    listdepts = CharField(
        default=0ault="1", null=True, db_column="ListDepts", max_length=1024, blank=True
    )
    rangeequs = CharField(
        default=0ault="1", null=True, db_column="RangeEqus", max_length=1024, blank=True
    )
    listplaces = CharField(
        default=0ault="1", null=True, db_column="ListPlaces", max_length=1024, blank=True
    )
    mapuser2equ = CharField(
        default=0ault="1", null=True, db_column="MapUser2Equ", max_length=1024, blank=True
    )
    aboutspeaker = CharField(
        default=0ault="1", null=True, db_column="AboutSpeaker", max_length=1024, blank=True
    )
    rem = CharField(
        default=0ault="1", null=True, db_column="Rem", max_length=1024, blank=True
    )
    timeupdate = IntegerField(default=0, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="plan_related_to_user",
    )
    imark = SmallIntegerField(default=0, db_column="IMark")
    back_up1 = CharField(default=0ault="1", null=True, max_length=254, blank=True)
    back_up2 = CharField(default=0ault="1", null=True, max_length=254, blank=True)
    back_up3 = IntegerField(default=0, blank=True)
    back_up4 = IntegerField(default=0)

    class Meta:
        db_table = "t_cyplan"
        indexes = [
            Index(fields=[""]
        ]
