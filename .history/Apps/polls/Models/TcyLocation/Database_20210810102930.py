from django.db.models import Model, CharField, ForeignKey, CASCADE,  IntegerField, ForeignKey, SmallIntegerField, OneToOneField,BigAutoField
from ..UserModel.Database import UserModel

class LocationModel(Model):
    id = BigAutoField(db_column='ID',
                             blank=True, primary_key=True)
    id_parent = IntegerField(default=0, null=True,
                                    db_column='ID_Parent', blank=True)
    name = CharField(default='0', null=True,
                            db_column='Name', max_length=128, blank=True)
    timeupdate = IntegerField(default=0, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    rem = CharField(default='0', null=True,
                           db_column='Rem', max_length=1024, blank=True)
    idmanager =  ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='location_related_to_user',db_constraint=False
    )
    imark = SmallIntegerField(default=0, null=True, db_column='IMark')
    rem = CharField(default='0', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)
    back_up3 = IntegerField(default=1, null=True)

    class Meta:
        db_table = 't_cylocation'

class LocationExtensionModel(Model):
    id_location = OneToOneField(
        LocationModel, to_field="id", on_delete=CASCADE, primary_key=True, db_column='ID_Location', related_name='locationex_related_to_location')
    attr = SmallIntegerField(
        default=1, null=True, db_column='Attr', blank=True)
    datebegin = IntegerField(default=1, null=True,
                                    db_column='DateBegin', blank=True)
    dateend = IntegerField(
        default=1, null=True, db_column='DateEnd', blank=True)
    moderun = IntegerField(
        default=1, null=True, db_column='ModeRun', blank=True)
    modeshangji = IntegerField(default=1, null=True,
                                      db_column='ModeShangJi', blank=True)
    enabledelaycharged = IntegerField(default=1, null=True,
                                             db_column='EnableDelayCharged', blank=True)
    delaycharged = IntegerField(default=1, null=True,
                                       db_column='DelayCharged', blank=True)
    enablelimityue_sj = IntegerField(default=1, null=True,
                                            db_column='EnableLimitYuE_SJ', blank=True)
    limityue_sj = IntegerField(default=1, null=True,
                                      db_column='LimitYuE_SJ', blank=True)
    enablelimityue_xj = IntegerField(default=1, null=True,
                                            db_column='EnableLimitYuE_XJ', blank=True)
    limityue_xj = IntegerField(default=1, null=True,
                                      db_column='LimitYuE_XJ', blank=True)
    enablelimittime_xj = IntegerField(default=1, null=True,
                                             db_column='EnableLimitTime_XJ', blank=True)
    limittime_xj = IntegerField(default=1, null=True,
                                       db_column='LimitTime_XJ', blank=True)
    enablewarnyue = IntegerField(default=1, null=True,
                                        db_column='EnableWarnYuE', blank=True)
    warnyue = IntegerField(
        default=1, null=True, db_column='WarnYuE', blank=True)
    enablewarntime = IntegerField(default=1, null=True,
                                         db_column='EnableWarnTime', blank=True)
    warntime = IntegerField(
        default=1, null=True, db_column='WarnTime', blank=True)
    enablemincost = IntegerField(default=1, null=True,
                                        db_column='EnableMinCost', blank=True)
    mincost = IntegerField(
        default=1, null=True, db_column='MinCost', blank=True)
    price = IntegerField(
        default=1, null=True, db_column='Price', blank=True)
    priceminute = IntegerField(default=1, null=True,
                                      db_column='PriceMinute', blank=True)
    getequname = IntegerField(default=1, null=True,
                                     db_column='GetEquName', blank=True
                                     )
    getequip = IntegerField(
        default=1, null=True, db_column='GetEquIp', blank=True)
    getequmac = IntegerField(default=1, null=True,
                                    db_column='GetEquMac', blank=True)
    timeupdate = IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True
                                     )
    idmanager =  ForeignKey(
        UserModel, to_field="id", on_delete=CASCADE, db_column='IdManager', related_name='locationex_related_to_user'
    )
    imark = SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = IntegerField(default=1, null=True, blank=True)
    back_up3 = IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cylocationex'
