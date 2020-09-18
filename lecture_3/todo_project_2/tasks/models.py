from django.db import models

# Create your models here.

# ORM - Object Relational Mapper
# takes your python objects, and stores them as database tables and rows
# Models for tables


# Low Level Design
# Requirements
# - [User] can add [Task]s
# - a task can be tagged with one or more [Tag]s
# - you can search for tasks by content, or by a tag
# - tasks can have an urgency and an importance
# - tasks can have a status - Pending, Completed, Dropped

# Detect nouns -> usually become entites/models
# Detect attributes and relationships

# model, view, controller are decoupled

# Django provides an id field to all model class by default
# makes the id field an integer, which autoincrements and is the primary key
# you can override
class Tag(models.Model):
    name = models.CharField(max_length=255)

 # Create an rich API for us for free

class Task(models.Model):  # class => table
    content = models.TextField()   # field => column in the table
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    class TaskStatus(models.TextChoices): # enumeration
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"
    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2,
    )  # must have restricted set of choices

# whenever I change my DB schema
# - my old DB is now useless
# - create a new DB?
# - somehow reenter the data in the new DB => hefty task
# - I don't want the users to renter the data
# Migration - Migrate the previous data to new DB
# approach 1 - delete DB, create new DB, enter data myself
# approach 2 - write a Migration script that looks at the prev DB,
#              and copies the data to the new DB
# Whenever I change my schema, I have to write this script again and again
# I have the previous DB schema
# I have the current models in Django
# Can I write a script that automatically find the differences and writes the migration
# script for me?
# django provides this out of the box



# 1 task can have 1 or more tags
# 1 tag (like shopping) can also have multiple tasks
# Many to Many Relationship

# Task_Tags =>
# id  | task_id (foreign key to tasks_task.id)  |  tag_id
#       (                 )

# OneToOne Relationship => column in your tables
# OneToMany Relationship => column in your tables
# ManyToOne Relationship => column in your tables
# ManyToMany Relationship => create a new table for this
