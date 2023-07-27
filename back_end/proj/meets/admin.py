from django.contrib import admin
from .models import Theme, Event, Client
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','date_time','theme')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Client, ClientAdmin)