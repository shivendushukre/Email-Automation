from django.contrib import admin
from .models import Detail


class DetailAdmin(admin.ModelAdmin):
    readonly_fields = ('time_of_sending',)


admin.site.register(Detail, DetailAdmin)
