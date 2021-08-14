from django.db.models import Model, CharField, ForeignKey, DateTimeField, TextField, IntegerField, BooleanField, ManyToManyField, OneToOneField, CASCADE,BigAutoField

class BaseModel(Model):
    id = BigAutoField(db_column="ID", primary_key=True, unique=True, blank=True)
    rem = CharField(default="0", null=True, db_column="Rem", max_length=64, blank=True)
    imark = IntegerField(default=0, null=True, db_column="IMark", blank=True)
    back_up1 = CharField(default="0", null=True, max_length=254, blank=True)
    back_up2 = IntegerField(default=0, null=True, blank=True)
    back_up3 = IntegerField(default=0, null=True, blank=True)
    timeupdate = IntegerField(default=0, null=True, db_column="TimeUpdate", blank=True)
    idmanager = IntegerField(default=0, null=True, db_column="IdManager", blank=True)
