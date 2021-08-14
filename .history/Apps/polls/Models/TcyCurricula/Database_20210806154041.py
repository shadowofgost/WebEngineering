from django.db import models
class CurriculaModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    timebegin = models.IntegerField(default=1, null=True,
                                    db_column='TimeBegin', blank=True)
    timeend = models.IntegerField(
        default=1, null=True, db_column='TimeEnd', blank=True)
    id_location = models. ForeignKey(
        LocationModel, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='curricula_related_to_location'
    )
    id_speaker = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='ID_Speaker', related_name='curricula_related_to_user_speaker'
    )
    attr = models.SmallIntegerField(
        default=1, null=True, db_column='Attr', blank=True)
    #####attr1代表实验类型、2代表普通上课类型、3讲座考勤类型，必须有值实验类型：奇数刷卡派位，偶数刷卡下机，并记录派位编号上课考勤类型：刷卡记录刷卡机编号讲座考勤类型：刷卡记录刷卡机编号######
    charge = models.SmallIntegerField(
        default=1, null=True, db_column='Charge', blank=True)
    ######charge免费0、收费1、开放2，必须有值######
    pwaccess = models.SmallIntegerField(
        default=1, null=True, db_column='PwAccess', blank=True)
    ######pwaccess不派位0、刷卡派位1（派位指用户刷卡时系统指定座位）######
    pwcontinuous = models.SmallIntegerField(default=1, null=True,
                                            db_column='PwContinuous', blank=True)
    ######pwcontinuous连续派位0、随机派位1######
    pwdirection = models.SmallIntegerField(default=1, null=True,
                                           db_column='PwDirection', blank=True)
    ######pwdirection顺序派位0、逆序派位1（当设置为随机派位时本功能无效）#######
    dooropen = models.SmallIntegerField(
        default=1, null=True, db_column='DoorOpen', blank=True)
    ######dooropen匹配的用户刷卡是否开门，0开门，1不开门######
    timebegincheckbegin = models.IntegerField(default=1, null=True,
                                              db_column='TimeBeginCheckBegin', blank=True)
    ######0代表无效######
    timebegincheckend = models.IntegerField(default=1, null=True,
                                            db_column='TimeBeginCheckEnd', blank=True)
    ######0代表无效######
    timeendcheckbegin = models.IntegerField(default=1, null=True,
                                            db_column='TimeEndCheckBegin', blank=True)
    ######0代表无效######
    timeendcheckend = models.IntegerField(default=1, null=True,
                                          db_column='TimeEndCheckEnd', blank=True)
    ######0代表无效######
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
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='curricula_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    bakc_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cycurricula'
