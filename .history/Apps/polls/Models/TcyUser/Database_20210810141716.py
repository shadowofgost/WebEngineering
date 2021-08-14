from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    BinaryField,
    EmailField,
    BigAutoField,
    Index,
)
from ..DepartmentModel.Database import DepartmentModel


class UserModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True,unique=True, blank=True)
    nocard = CharField(default="0", null=True, db_column="Nocard", max_length=32)
    nouser = CharField(default="0", null=True, db_column="NoUser", max_length=32)
    name = CharField(default="0", null=True, db_column="Name", max_length=32)
    psw = CharField(default="0", null=True, db_column="Psw", max_length=32)
    deptid = ForeignKey(
        DepartmentModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="Deptid",
        related_name="related_to_department",
        db_constraint=False,
    )
    """
    sex_choices=[
        (0,"女"),
        (1,"男"),
    ]
    """
    """
    sex = SmallIntegerField(default=1, null=True, db_column="Sex",choices=sex_choices)
    """
    sex = SmallIntegerField(default=1, null=True, db_column="Sex")
    ##########sex 的值只能为0（女）或者1（男）##########
    """
    attr_choices=[
        (0,"超级管理员"),
        (1,"管理员"),
        (2,"")
    ]
    """
    attr = SmallIntegerField(default=1, null=True, db_column="Attr")
    ##########attr 用户管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    attrjf = SmallIntegerField(default=1, null=True, db_column="AttrJf")
    ##########机房管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    yue = IntegerField(default=1, null=True, db_column="Yue")
    ##用户余额1，单位为分；（默认）##
    yue2 = IntegerField(default=1, null=True, db_column="Yue2")
    ##用户余额2，单位为分；（扩展于特殊需求）##
    email = EmailField(default=None, null=True, db_column="Email", max_length=254)
    phone = IntegerField(default=1, null=True, db_column="Phone")
    timeupdate = IntegerField(default=1, null=True, db_column="TimeUpdate")
    idmanager = IntegerField(default=1, null=True, db_column="IdManager", blank=True)
    localid = CharField(default="1", null=True, db_column="LocalID", max_length=1024)
    rem = CharField(default="1", null=True, db_column="Rem", max_length=64)
    imark = IntegerField(default=1, null=True, db_column="IMark")
    back_up1 = CharField(default="1", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)
    back_up3 = IntegerField(default=1, null=True)

    class Meta:
        db_table = "t_cyuser"


class UserExtensionModel(Model):
    id = OneToOneField(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        primary_key=True,
        db_column="ID",
        related_name="userex_related_to_user_information",
    )
    rem = CharField(
        default="1",
        null=True,
        db_column="Rem",
        max_length=32,
        blank=True,
    )
    photo = BinaryField(db_column="FaceFearture", blank=True)
    timeupdate = IntegerField(default=1, null=True, db_column="TimeUpdate", blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="userex_related_to_user",
    )
    imark = IntegerField(default=1, null=True, db_column="IMark")
    rem = CharField(default="1", null=True, db_column="Rem", max_length=64)
    back_up1 = CharField(default="1", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)
    back_up3 = IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = "t_cyuserex"
