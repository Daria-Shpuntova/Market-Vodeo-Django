# Generated by Django 4.2.6 on 2023-12-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_direction_remove_direction_course_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='direction',
            field=models.ManyToManyField(null=True, to='courses.direction'),
        ),
    ]
