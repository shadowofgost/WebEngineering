"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:53:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/Apps/polls/Models/TableInformationModel/Database.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:15:47
# @Software         : Vscode
"""
from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    ForeignKey,
    Index,
)
from ..UserModel.Database import UserModel
from ..Public.Database import BaseModel

class TableInformationModel(BaseModel):
    name = CharField(default="0", null=True, db_column="Name", max_length=50,blank=True)
    nametable = CharField(default="0", null=True, db_column="NameTable", max_length=50,blank=True)
    idmanager = ForeignKey(
        UserModel,
        to_field="id",
        on_delete=CASCADE,
        db_column="IdManager",
        related_name="kaoqin_related_to_user",
        db_constraint=False,
    )

    class Meta:
        db_table = "t_cytableinfo"
