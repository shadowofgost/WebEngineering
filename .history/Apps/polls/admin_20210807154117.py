from django.contrib import admin
from . import models


admin.site.register(models.UserModel)
admin.site.register(models.DepartmentModel)
admin.site.register(models.UserExtensionModel)
admin.site.register(models.RunningAccountModel)
admin.site.register(models.MmxDataModel)
admin.site.register(models.EquipmentModel)
admin.site.register(models.TableInformationModel)
admin.site.register(models.MmxModel)
admin.site.register(models.LocationModel)
admin.site.register(models.LocationExtensionModel)
admin.site.register(models.TyperaModel)
admin.site.register(models.CurriculaModel)
admin.site.register(models.CoursePlanModel)
# Register your models here.
