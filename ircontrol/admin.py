from django.contrib import admin

# Register your models here.
from .models import *



class DeviceActionInline(admin.TabularInline):
	model = DeviceAction
	extra = 1
	ordering= ("layout_row", "layout_col")
	
class DeviceAdmin(admin.ModelAdmin):
	inlines = [
        DeviceActionInline
    ]

admin.site.register(Device, DeviceAdmin)	
admin.site.register(DeviceAction)	
