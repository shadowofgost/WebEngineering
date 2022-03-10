"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:53:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/Apps/polls/Models/DepartmentModel/Database.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:15:15
# @Software         : Vscode
"""
from django.db.models import (
    CharField,
    IntegerField,
    Index
)
from ..Public.Database import BaseModel
# Create your models here.


class DepartmentModel(BaseModel):
    id_parent = IntegerField(default=0, null=True, db_column="ID_Parent", blank=True)
    name = CharField(
        default="0", null=True, db_column="Name", max_length=32, blank=True
    )
    idmanager = IntegerField(default=0, null=True, db_column="IdManager", blank=True)

    class Meta:
        db_table = "t_cydept"