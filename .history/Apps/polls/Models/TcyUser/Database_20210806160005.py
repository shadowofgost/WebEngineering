from django.db import models
from ..DepartmentModel.Database import DepartmentModel
class UserModel(models.Model):
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
        DepartmentModel, to_field="id", on_delete=models.CASCADE,  db_column='Deptid', related_name='related_to_department')
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
class UserExtensionModel(models.Model):
    id = models.OneToOneField(
        UserModel, to_field="id", on_delete=models.CASCADE, primary_key=True, db_column='ID', related_name='userex_related_to_user_information')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=32, blank=True,)
    photo = models.BinaryField(db_column='FaceFearture', blank=True)
    timeupdate = models.IntegerField(default=1, null=True,
                                     db_column='TimeUpdate', blank=True)
    idmanager = models.ForeignKey(
        UserModel, to_field="id", on_delete=models.CASCADE, db_column='IdManager', related_name='userex_related_to_user')
    imark = models.IntegerField(default=1, null=True, db_column='IMark')
    rem = models.CharField(default='1', null=True,
                           db_column='Rem', max_length=64)
    back_up1 = models.CharField(default='1', null=True,
                                max_length=254, blank=True)
    back_up2 = models.IntegerField(default=1, null=True, blank=True)
    back_up3 = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 't_cyuserex'
