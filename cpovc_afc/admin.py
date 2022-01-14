from django.contrib import admin
from .models import AFCMain, AFCForms, AFCEvents


class AFCMainAdmin(admin.ModelAdmin):
    """Admin back end for Geo data management."""

    search_fields = ['case_number', 'person__surname', 'person__first_name']
    list_display = ['case_id', 'case_number', 'person',
                    'case_date', 'get_creator', 'case_status', 'case_stage']
    # readonly_fields = ['area_id']
    list_filter = ['is_void', 'case_status', 'case__created_by']

    def get_creator(self, obj):
        return obj.case.created_by
    get_creator.short_description = 'Creator'
    get_creator.admin_order_field = 'case__created_by'
    # actions = [dump_to_csv]


admin.site.register(AFCMain, AFCMainAdmin)


class FormsInline(admin.StackedInline):
    model = AFCForms


class AFCEventsAdmin(admin.ModelAdmin):
    """Admin back end for Geo data management."""

    search_fields = ['person_id']
    list_display = ['case_id', 'form_id', 'event_date']
    # readonly_fields = ['area_id']
    list_filter = ['is_void', 'event_date']

    inlines = (FormsInline, )


admin.site.register(AFCEvents, AFCEventsAdmin)
