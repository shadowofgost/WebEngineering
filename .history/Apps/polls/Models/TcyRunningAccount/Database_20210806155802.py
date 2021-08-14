from django.db import models
from ..UserModel.Database import UserModel
from ..CoursePlanModel.Database import CoursePlanModel
class RunningAccountModel(models.Model):
    id = models.IntegerField(default=1, db_column='ID',
                             blank=True, primary_key=True)
    id_user = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='ID_User', related_name='runningaccount_related_to_user_use')
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
        CoursePlanModel, to_field="id", on_delete=models.CASCADE, db_column='Param2', related_name='runningaccount_related_to_plan')
    ######param2取消交易记录的ID： Type=0x106,讲座、课程编号： Type = 0x201、0x1001######
    timeupdate = models.IntegerField(default=1, null=True, db_column='TimeUpdate',
                                     blank=True)
    idmanager = models. ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='runningaccount_related_to_user')
    imark = models.SmallIntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cyrunningaccount'
