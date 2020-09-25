from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class TaskStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    COMPLETED = 'CO', 'Completed'
    DROPPED = 'DR', 'Dropped'


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    completed_at = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.content}'

    def get_all_tags(self, delimiter=', '):
        return delimiter.join([tag.name for tag in self.tags.all()])
