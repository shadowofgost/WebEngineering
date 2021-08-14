from django.contrib import admin
from .Models.UserModel.Database import UserModel,UserExtensionModel
from .Models.DepartmentModel.Database import DepartmentModel
from .Models.RunningAccountModel.Database import RunningAccountModel
from .Models.CurriculaModel.Database import CurriculaModel
from .Models.MmxModel.Database import MmxModel,MmxDataModel
from .Models.EquipmentModel.Database import EquipmentModel
from .Models.TableInformationModel.Database import TableInformationModel
from .Models.LocationModel.Database import LocationModel,LocationExtensionModel
from .Models.CoursePlanModel.Database import CoursePlanModel
from .Models.TyperaModel.Database import TyperaModel


admin.site.register(UserModel)
admin.site.register(DepartmentModel)
admin.site.register(UserExtensionModel)
admin.site.register(RunningAccountModel)
admin.site.register(MmxDataModel)
admin.site.register(EquipmentModel)
admin.site.register(TableInformationModel)
admin.site.register(MmxModel)
admin.site.register(LocationModel)
admin.site.register(LocationExtensionModel)
admin.site.register(TyperaModel)
admin.site.register(CurriculaModel)
admin.site.register(CoursePlanModel)
# Register your models here.
