from django.db import models

# Create your models here.


class TCydept(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    id_parent = models.IntegerField(
        default=1, null=True, db_column='ID_Parent')
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32)
    timeupdate = models.IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    idmanager = models.IntegerField(
        default=1, null=True, db_column='IdManager')
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    bakc_up1 = models.CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True,  blank=True)

    class Meta:
        db_table = 't_cydept'


class TCyuser(models.Model):
    id = models.IntegerField(default=1, db_column='ID', primary_key=True)
    nocard = models.CharField(default='1', null=True,
                              db_column='Nocard', max_length=32)
    nouser = models.CharField(default='1', null=True,
                              db_column='NoUser', max_length=32)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32)
    psw = models.CharField(default='1', null=True,
                           db_column='Psw', max_length=32)
    deptid = models. ForeignKey(
        TCydept, to_field="id", on_delete=models.CASCADE,  db_column='Deptid', related_name='related_to_department')
    sex = models.SmallIntegerField(default=1, null=True, db_column='Sex')
    ##########sex 的值只能为0（女）或者1（男）##########
    attr = models.SmallIntegerField(default=1, null=True, db_column='Attr')
    ##########attr 用户管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    attrjf = models.SmallIntegerField(default=1, null=True, db_column='AttrJf')
    ##########机房管理权限， 0普通用户、1管理员、2超级管理员（可对管理员进行管理）##########
    yue = models.IntegerField(default=1, null=True, db_column='Yue')
    ##用户余额1，单位为分；（默认）##
    yue2 = models.IntegerField(default=1, null=True, db_column='Yue2')
    ##用户余额2，单位为分；（扩展于特殊需求）##
    email = models.EmailField(default=None, null=True,
                              db_column='Email', max_length=254)
    phone = models.IntegerField(default=1, null=True, db_column='Phone')
    timeupdate = models.IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    idmanager = models.IntegerField(default=1, null=True,
                                    db_column='IdManager', blank=True)
    localid = models.CharField(
        default='1', null=True,  db_column='LocalID', max_length=1024)
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    imark = models.IntegerField(default=1, null=True, db_column='IMark')
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cyuser'


class TCylocation(models.Model):
    id = models.IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_parent = models.IntegerField(default=1, null=True,
                                    db_column='ID_Parent', blank=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=1024, blank=True)
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='location_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cylocation'


class TCycurricula(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    timebegin = models.IntegerField(default=1, null=True,
                                    db_column='TimeBegin', blank=True)
    timeend = models.IntegerField(
        default=1, null=True, db_column='TimeEnd', blank=True)
    id_location = models. ForeignKey(
        TCylocation, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='curricula_related_to_location'
    )
    id_speaker = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='ID_Speaker', related_name='curricula_related_to_user_speaker'
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
                                  db_column='RangeUsers', max_length=4096, blank=True)
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
    # 来自教务系统的课程编号
    timeupdate = models.IntegerField(default=1, null=True, db_column='TimeUpdate',
                                     blank=True)
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='curricula_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    bakc_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cycurricula'


class TCyplan(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             primary_key=True, blank=True)
    id_curricula = models. ForeignKey(
        TCycurricula, to_field="id", on_delete=models.CASCADE,
        db_column='ID_Curricula', related_name='id_curricula'
    )
    timebegin = models.IntegerField(default=1, null=True,
                                    db_column='TimeBegin', blank=True
                                    )
    timeend = models.IntegerField(
        default=1, null=True, db_column='TimeEnd', blank=True)
    id_location = models. ForeignKey(
        TCylocation, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='plan_related_to_location'
    )
    id_speaker = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE,  db_column='ID_Speaker', related_name='plan_related_to_user_speaker'
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
                                  db_column='RangeUsers', max_length=4096, blank=True)
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
                           db_column='Rem', max_length=1024, blank=True)  # 来自教务系统的课程编号
    timeupdate = models.IntegerField(default=1, null=True, db_column='TimeUpdate',
                                     blank=True)
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE,  db_column='IdManager', related_name='plan_related_to_user', null=True)
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)
    back_up4 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cyplan'


class TCyequipment(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             blank=True, primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    id_location = models. ForeignKey(
        TCylocation, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='equipment_related_to_location')
    id_location_sn = models.SmallIntegerField(default=1, null=True,
                                              db_column='ID_Location_SN', blank=True)
    id_ip = models.CharField(default='1', null=True,
                             db_column='ID_IP', max_length=16, blank=True)
    mac = models.CharField(default='1', null=True,
                           db_column='MAC', max_length=24, blank=True)
    state = models.SmallIntegerField(
        default=1, null=True, db_column='State', blank=True)
    ########state设备状态，0：正常空闲、1：故障、2：其它、3：正常使用中、4开放########
    login = models.SmallIntegerField(
        default=1, null=True, db_column='Login', blank=True)
    ########login登录状态，0：未登录、1：已经登录########
    link = models.SmallIntegerField(
        default=1, null=True, db_column='Link', blank=True)
    # link网络状态，0：脱机、1：在线，######## Field renamed because it was a Python reserved word.
    class_field = models.SmallIntegerField(
        default=1, null=True, db_column='Class', blank=True)
    ########class_field0：PC设备、2：刷卡设备，11:服务器设备#######
    dx = models.IntegerField(default=1, null=True, db_column='Dx', blank=True)
    dy = models.IntegerField(default=1, null=True, db_column='Dy', blank=True)
    id_user = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='ID_User', related_name='equipment_related_to_user_use')
    id_plan = models.IntegerField(
        default=1, null=True, db_column='ID_Plan', blank=True)
    itimebegin = models.IntegerField(default=1, null=True,
                                     db_column='iTimeBegin', blank=True
                                     )
    itimelogin = models.IntegerField(default=1, null=True,
                                     db_column='iTimeLogin', blank=True
                                     )
    whitelist = models.CharField(default='1', null=True,
                                 db_column='WhiteList', max_length=1024, blank=True)
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=1024, blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='equipment_related_to_user', null=True
    )
    portlisten = models.IntegerField(default=1, null=True,
                                     db_column='PortListen', blank=True
                                     )
    type_field = models.IntegerField(
        default=1, null=True, db_column='Type', blank=True)
    timedelay = models.IntegerField(default=1, null=True,
                                    db_column='TimeDelay', blank=True)
    keycancel = models.SmallIntegerField(default=1, null=True,
                                         db_column='KeyCancel', blank=True)
    keyOk = models.SmallIntegerField(
        default=1, null=True, db_column='KeyOk', blank=True)
    keydel = models.SmallIntegerField(
        default=1, null=True, db_column='KeyDel', blank=True)
    keyf1 = models.SmallIntegerField(
        default=1, null=True, db_column='KeyF1', blank=True)
    onall = models.SmallIntegerField(
        default=1, null=True, db_column='OnAll', blank=True)
    rangeequs = models.CharField(default='1', null=True,
                                 db_column='RangeEqus', max_length=64, blank=True)
    listplaces = models.CharField(default='1', null=True,
                                  db_column='ListPlaces', max_length=64, blank=True)
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cyequipment'


class TCyTableInfo(models.Model):
    id = models.IntegerField(default=1,  db_column='ID', primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=50)
    nametable = models.CharField(
        default='1', null=True,  db_column='NameTable', max_length=50)
    timeupdate = models.IntegerField(
        default=1, null=True, db_column='TimeUpdate')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='kaoqin_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    back_up1 = models.CharField(
        default='1', null=True,  max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cytableinfo'


class TCylocationex(models.Model):
    id_location = models.OneToOneField(
        TCylocation, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID_Location', related_name='locationex_related_to_location')
    attr = models.SmallIntegerField(
        default=1, null=True, db_column='Attr', blank=True)
    datebegin = models.IntegerField(default=1, null=True,
                                    db_column='DateBegin', blank=True)
    dateend = models.IntegerField(
        default=1, null=True, db_column='DateEnd', blank=True)
    moderun = models.IntegerField(
        default=1, null=True, db_column='ModeRun', blank=True)
    modeshangji = models.IntegerField(default=1, null=True,
                                      db_column='ModeShangJi', blank=True)
    enabledelaycharged = models.IntegerField(default=1, null=True,
                                             db_column='EnableDelayCharged', blank=True)
    delaycharged = models.IntegerField(default=1, null=True,
                                       db_column='DelayCharged', blank=True)
    enablelimityue_sj = models.IntegerField(default=1, null=True,
                                            db_column='EnableLimitYuE_SJ', blank=True)
    limityue_sj = models.IntegerField(default=1, null=True,
                                      db_column='LimitYuE_SJ', blank=True)
    enablelimityue_xj = models.IntegerField(default=1, null=True,
                                            db_column='EnableLimitYuE_XJ', blank=True)
    limityue_xj = models.IntegerField(default=1, null=True,
                                      db_column='LimitYuE_XJ', blank=True)
    enablelimittime_xj = models.IntegerField(default=1, null=True,
                                             db_column='EnableLimitTime_XJ', blank=True)
    limittime_xj = models.IntegerField(default=1, null=True,
                                       db_column='LimitTime_XJ', blank=True)
    enablewarnyue = models.IntegerField(default=1, null=True,
                                        db_column='EnableWarnYuE', blank=True)
    warnyue = models.IntegerField(
        default=1, null=True, db_column='WarnYuE', blank=True)
    enablewarntime = models.IntegerField(default=1, null=True,
                                         db_column='EnableWarnTime', blank=True)
    warntime = models.IntegerField(
        default=1, null=True, db_column='WarnTime', blank=True)
    enablemincost = models.IntegerField(default=1, null=True,
                                        db_column='EnableMinCost', blank=True)
    mincost = models.IntegerField(
        default=1, null=True, db_column='MinCost', blank=True)
    price = models.IntegerField(
        default=1, null=True, db_column='Price', blank=True)
    priceminute = models.IntegerField(default=1, null=True,
                                      db_column='PriceMinute', blank=True)
    getequname = models.IntegerField(default=1, null=True,
                                     db_column='GetEquName', blank=True
                                     )
    getequip = models.IntegerField(
        default=1, null=True, db_column='GetEquIp', blank=True)
    getequmac = models.IntegerField(default=1, null=True,
                                    db_column='GetEquMac', blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='locationex_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cylocationex'


class TCymmx(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             blank=True, primary_key=True)
    id_data = models.IntegerField(
        default=1, null=True, db_column='ID_Data', blank=True)
    id_type = models.SmallIntegerField(
        default=1, null=True, db_column='ID_Type', blank=True)
    ######id_type字段为媒体类型，1为PPT类型######
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models.ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='mmx_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmx'


class TCymmxdata(models.Model):
    id = models.OneToOneField(
        TCymmx, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID', related_name='mmxdata_related_to_mmx'
    )
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='mmxdata_related_to_user', null=True
    )
    data = models.TextField(db_column='Data', blank=True)
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cymmxdata'


class TCyRunningaccount(models.Model):
    id = models.IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_user = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='ID_User', related_name='runningaccount_related_to_user_use')
    # 0表示缺席，1表示签到，2表示签退
    time = models.IntegerField(
        default=1, null=True, db_column='Time', blank=True)
    type_field = models.SmallIntegerField(
        default=1, null=True, db_column='Type', blank=True)
    ######type例如：交费、存款：0x101，赠费： 0x102，退费、取款：0x103，扣费、罚款：0x104，纠错，取消某次缴费、赠费等：0x106，上机费： 0x201,考勤： 0x1001######
    money = models.IntegerField(
        default=1, null=True, db_column='Money', blank=True)
    ######money发生的费用，单位为分#####
    param1 = models.IntegerField(
        default=1, null=True, db_column='Param1', blank=True)
    ######param1收费管理员的ID：Type=0x101、0x102、0x103、0x104、0x106,上机机位编号： Type = 0x201,门禁考勤机编号：Type = 0x1001######
    param2 = models.ForeignKey(
        TCyplan, to_field="id", on_delete=models.CASCADE, db_column='Param2', related_name='runningaccount_related_to_plan')
    ######param2取消交易记录的ID： Type=0x106,讲座、课程编号： Type = 0x201、0x1001######
    timeupdate = models.IntegerField(default=1, null=True, db_column='TimeUpdate',
                                     blank=True)
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='runningaccount_related_to_user', null=True)
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cyrunningaccount'


class TCytypera(models.Model):
    id = models.IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_parent = models.IntegerField(default=1, null=True,
                                    db_column='ID_Parent', blank=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager = models. ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='typera_related_to_user', null=True
    )
    imark = models.SmallIntegerField(
        default=1, null=True, db_column='IMark')  # 1代表已经删除
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cytypera'


class TCyuserex(models.Model):
    id = models.OneToOneField(
        TCyuser, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID', related_name='userex_related_to_user_information')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=32, blank=True,)
    photo = models.BinaryField(db_column='FaceFearture', blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True)
    idmanager = models.ForeignKey(
        TCyuser, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='userex_related_to_user', null=True)
    imark = models.IntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cyuserex'
