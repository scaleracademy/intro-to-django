from django.db import models
from django.utils import timezone


class TaskStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    COMPLETED = 'CO', 'Completed'
    DROPPED = 'DR', 'Dropped'


class Tag(models.Model):
    name = models.CharField(max_length=255)

    # magic methods
    # dunder => double underscore method in python

    def __str__(self):
        # object.toString() in the java world
        # gives a human readable representation of the object
        return self.name

class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    completed_at = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    # null is False => NOT NULL
    # null => database thing - it is okay for this column to have a null val
    # blank => validation - it is okay if the user doesn't provide this field

    status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    @property  # properties and descriptor protocol in Python
    def foo(self):
        return 'hello'

    def __str__(self):
        return f'{self.content}'
