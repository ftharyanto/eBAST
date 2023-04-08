from django.contrib import admin
from ChecklistSeiscomp.models import ChecklistSeiscompModel, OperatorModel, StationListModel

# Register your models here.

admin.site.register(ChecklistSeiscompModel)
admin.site.register(OperatorModel)
admin.site.register(StationListModel)