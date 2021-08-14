from django.db import models
from ..UserModel.Database import UserModel
from ..CurriculaModel.Database import CurriculaModel
from ..LocationModel.Database import LocationModel
class CoursePlanModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             primary_key=True, blank=True)
    id_curricula = models. ForeignKey(
        CurriculaModel, to_field="id", on_delete=models.CASCADE,
        db_column='ID_Curricula', related_name='id_curricula'
    )
    timebegin = models.IntegerField(default=1, null=True,
                                    db_column='TimeBegin', blank=True
                                    )
    timeend = models.IntegerField(
        default=1, null=True, db_column='TimeEnd', blank=True)
    id_location = models. ForeignKey(
        LocationModel, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='plan_related_to_location'
    )
    id_speaker = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE,  db_column='ID_Speaker', related_name='plan_related_to_user_speaker'
    )
    attr = models.SmallIntegerField(
        default=1, null=True, db_column='Attr', blank=True)
    charge = models.SmallIntegerField(
        default=1, null=True, db_column='Charge', blank=True)
    pwaccess = models.SmallIntegerField(
        default=1, null=True, db_column='PwAccess', blank=True)
    pwcontinuous = models.SmallIntegerField(default=1, null=True,
                                            db_column='PwContinuous', blank=True)
    pwdirection = models.SmallIntegerField(default=1, null=True,
                                           db_column='PwDirection', blank=True)
    dooropen = models.SmallIntegerField(
        default=1, null=True, db_column='DoorOpen', blank=True)
    timebegincheckbegin = models.IntegerField(default=1, null=True, db_column='TimeBeginCheckBegin',
                                              blank=True)
    timebegincheckend = models.IntegerField(default=1, null=True,
                                            db_column='imeBeginCheckEnd', blank=True)
    timeendcheckbegin = models.IntegerField(default=1, null=True,
                                            db_column='TimeEndCheckBegin', blank=True)
    timeendcheckend = models.IntegerField(default=1, null=True,
                                          db_column='TimeEndCheckEnd', blank=True)
    rangeusers = models.CharField(default='1', null=True,
                                  db_column='RangeUsers', max_length=1024, blank=True)
    listdepts = models.CharField(default='1', null=True,
                                 db_column='ListDepts', max_length=1024, blank=True)
    rangeequs = models.CharField(default='1', null=True,
                                 db_column='RangeEqus', max_length=1024, blank=True)
    listplaces = models.CharField(default='1', null=True,
                                  db_column='ListPlaces', max_length=1024, blank=True)
    mapuser2equ = models.CharField(default='1', null=True,
                                   db_column='MapUser2Equ', max_length=1024, blank=True)
    aboutspeaker = models.CharField(default='1', null=True,
                                    db_column='AboutSpeaker', max_length=1024, blank=True)
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=1024, blank=True)
    timeupdate = models.IntegerField(default=1, null=True, db_column='TimeUpdate',
                                     blank=True)
    idmanager = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE,  db_column='IdManager', related_name='plan_related_to_user')
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)
    back_up4 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cyplan'
