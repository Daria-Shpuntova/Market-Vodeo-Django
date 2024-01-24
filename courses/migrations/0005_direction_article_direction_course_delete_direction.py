# Generated by Django 4.2.6 on 2023-12-06 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_articles_name_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_article', models.CharField(max_length=100, verbose_name='Название направления')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.articles')),
            ],
            options={
                'verbose_name': 'Направление статьи',
                'verbose_name_plural': 'Направления статей',
            },
        ),
        migrations.CreateModel(
            name='Direction_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_course', models.CharField(max_length=100, verbose_name='Название направления')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
            options={
                'verbose_name': 'Направление курса',
                'verbose_name_plural': 'Направления курсов',
            },
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
    ]
