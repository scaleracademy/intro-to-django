from django.contrib import admin
from django.utils import timezone

from . import models


def mark_complete(model_admin, request, queryset):
    queryset.update(
        status=models.TaskStatus.COMPLETED,
        completed_at=timezone.now(),
    )


def mark_pending(model_admin, request, queryset):
    queryset.update(
        status=models.TaskStatus.PENDING,
        completed_at=None,
    )


mark_complete.short_description = 'Mark these tasks as completed right now.'
mark_pending.short_description = 'Mark these tasks as pending.'


class TaskAdmin(admin.ModelAdmin):
    fields = [
        'content',
        'deadline',
        'tags'
    ]
    list_display = ['content', 'status', 'deadline', 'get_all_tags']
    list_editable = ['status']
    actions = [mark_complete, mark_pending]
    list_filter = ['status', 'deadline', 'tags']
    search_fields = ['content', 'tags__name']

    ordering = ['status', 'deadline']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Tag, TagAdmin)
