"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:53:49
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/Apps/polls/Models/Public/Database.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:33:26
# @Software         : Vscode
"""
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    BigAutoField,
)

class BaseModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True, unique=True, blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    imark = IntegerField(default=0, null=True, db_column="IMark", blank=True)
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)
    back_up3 = IntegerField(default=0, null=True, blank=True)
    class Meta:
        abstract = True
