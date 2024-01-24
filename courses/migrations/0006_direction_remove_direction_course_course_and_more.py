# Generated by Django 4.2.6 on 2023-12-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_direction_article_direction_course_delete_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=100, verbose_name='Название направления')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.RemoveField(
            model_name='direction_course',
            name='course',
        ),
        migrations.DeleteModel(
            name='Direction_article',
        ),
        migrations.DeleteModel(
            name='Direction_course',
        ),
    ]
