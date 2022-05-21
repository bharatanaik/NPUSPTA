from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from import_export.admin import ExportActionModelAdmin
from main.models import *


admin.site.site_title = "NPUSPTA"
admin.site.site_header = "NPUSPTA"

class FreeCounsellingAdmin(ExportActionModelAdmin):
    list_filter = ('stream', 'Class')

admin.site.register(FreeCounselling , FreeCounsellingAdmin)


class ScholorshipAdmin(ExportActionModelAdmin):
    pass


class MembershipTeacherAdmin(ExportActionModelAdmin):
    pass

class Membership10thAdmin(ExportActionModelAdmin):
    pass

class Membership12thAdmin(ExportActionModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Scholorship, ScholorshipAdmin)
admin.site.register(MembershipTeacher, MembershipTeacherAdmin)
admin.site.register(Membership10th, Membership10thAdmin)
admin.site.register(Membership12th, Membership12thAdmin)
# admin.site.register(AssistanceChoices)
admin.site.register(Notice)