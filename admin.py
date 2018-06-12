from django.contrib import admin

from .models import Portfolio, Service, Service2, Service3, Event, InfernoeTeam

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
            ( None, {'fields':['project_name','category','client','intro_text','date','project_description','image']})
                ]
    list_display = ('project_name','category','client','date')

    list_filter = ['date']

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
            ( None, {'fields':['event','date','event_info','image']})
                ]
    list_display = ('event','date')

    list_filter = ['date']



admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Service)
admin.site.register(Service2)
admin.site.register(Service3)
admin.site.register(Event,EventAdmin)
admin.site.register(InfernoeTeam)
