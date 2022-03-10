"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:53:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/Apps/polls/Models/TyperaModel/Database.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:15:52
# @Software         : Vscode
"""
from django.db.models import (
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
from ..Public.Database import BaseModel

class TyperaModel(BaseModel):
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=128, blank=True
    )
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="typera_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cytypera"
