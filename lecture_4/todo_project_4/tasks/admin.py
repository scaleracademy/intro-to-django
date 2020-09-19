from django.contrib import admin
from django.utils import timezone

from . import models
# Register your models here.

def mark_complete(model_admin, request, queryset):
    queryset.update(
        status=models.TaskStatus.COMPLETED,
        completed_at=timezone.now(),
    )
mark_complete.short_description = 'Mark these tasks as completed right now.'


def mark_pending(model_admin, request, queryset):
    queryset.update(
        status=models.TaskStatus.PENDING,
        completed_at=None,
    )
mark_pending.short_description = 'Mark these tasks as pending.'

class TaskAdmin(admin.ModelAdmin):
    fields = [
        ('content', 'deadline'),
        'tags'
    ]

    list_display = ['content', 'status', 'deadline']  # this allows me to render additional attributes
    list_editable = ['status']
    actions = [mark_complete, mark_pending]
    list_filter = ['status', 'deadline', 'tags']
    search_fields = ['content', 'tags__name']
    # ordering = ['status']

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['status']
        else:
            return ['deadline']


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Tag)
