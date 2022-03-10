"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:53:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/Apps/polls/Models/MmxModel/Database.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:21:17
# @Software         : Vscode
"""
from django.db.models import (
    ForeignKey,
    CASCADE,
    IntegerField,
    ForeignKey,
    SmallIntegerField,
    OneToOneField,
    TextField,
    Index,
)
from ..UserModel.Database import UserModel
from ..Public.Database import BaseModel


class MmxModel(BaseModel):
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
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmx_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cymmx"


class MmxDataModel(BaseModel):
    id_mmxdata = OneToOneField(
        MmxModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="ID_mmxdata",
        related_name="mmxdata_related_to_mmx",
        db_constraint=False,
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="mmxdata_related_to_user",
        db_constraint=False,
    )
    data = TextField(db_column="Data", blank=True)

    class Meta:
        db_table = "t_cymmxdata"
