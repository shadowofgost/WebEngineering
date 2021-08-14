from django.db import models
from ..UserModel.Database import UserModel
from ..LocationModel.Database import LocationModel
class EquipmentModel(models.Model):
    id = models.IntegerField(default=1,  db_column='ID',
                             blank=True, primary_key=True)
    name = models.CharField(default='1', null=True,
                            db_column='Name', max_length=32, blank=True)
    id_location = models. ForeignKey(
        LocationModel, to_field="id", on_delete=models.CASCADE, db_column='ID_Location', related_name='equipment_related_to_location')
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
    ########class_field0：PC设备、2：刷卡设备，#######
    dx = models.IntegerField(default=1, null=True, db_column='Dx', blank=True)
    dy = models.IntegerField(default=1, null=True, db_column='Dy', blank=True)
    id_user = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='ID_User', related_name='equipment_related_to_user_use')
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
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='equipment_related_to_user'
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
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cyequipment'
