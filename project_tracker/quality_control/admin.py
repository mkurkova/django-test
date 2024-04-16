from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description') 
    list_editable = ('status',)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Information about bug', {
            'fields': ('project', 'task', 'status', 'priority')
        })
    )


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description') 
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Information about request', {
            'fields': ('project', 'task', 'status', 'priority')
        })
    )
