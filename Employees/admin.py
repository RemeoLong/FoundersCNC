from django.contrib import admin
from Employees.models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('company', 'address', 'city', 'state', 'zip_code', 'contact_first_name',
                    'contact_last_name', 'phone_number')


class MachineBrandAdmin(admin.ModelAdmin):
    list_display = ('brand', )


class MachineModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model')


class RevisionAdmin(admin.ModelAdmin):
    list_display = ('machine_id', 'revision', 'file')


class MachineDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'document', 'created_at')


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zip_code', 'contact_first_name', 'contact_last_name',
                    'phone_number')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(MachineBrand, MachineBrandAdmin)
admin.site.register(MachineModel, MachineModelAdmin)
admin.site.register(Revision, RevisionAdmin)
admin.site.register(MachineDocument, MachineDocumentAdmin)
admin.site.register(Merchant, MerchantAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Company, CompanyAdmin)

