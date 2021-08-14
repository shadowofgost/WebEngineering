from django.db import models
from ..UserModel.Database import UserModel

class LocationModel(models.Model):
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
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='location_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cylocation'

class LocationExtensionModel(models.Model):
    id_location = models.OneToOneField(
        LocationModel, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID_Location', related_name='locationex_related_to_location')
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
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='locationex_related_to_user'
    )
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cylocationex'
