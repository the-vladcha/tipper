from django.contrib import admin

from calculator.models import Tippers, Storages


class TipperAdmin(admin.ModelAdmin):
    fields = ('board_number', 'model', 'max_load_capacity', 'cargo', 'cargo_characteristics')


class StorageAdmin(admin.ModelAdmin):
    fields = ('name', 'fullness', 'poly', 'cargo_characteristics')


admin.site.register(Tippers, TipperAdmin)
admin.site.register(Storages, StorageAdmin)
