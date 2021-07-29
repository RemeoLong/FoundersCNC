from django.contrib import admin
from Employees.models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('company', 'address', 'city', 'state', 'zip_code', 'contact_first_name',
                    'contact_last_name', 'phone_number')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'brand', 'model')


class RevisionAdmin(admin.ModelAdmin):
    list_display = ('machine_id', 'revision', 'file')


class MachineDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'document', 'created_at')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Revision, RevisionAdmin)
admin.site.register(MachineDocument, MachineDocumentAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)

