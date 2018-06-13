# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 19:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangoUserExtension', '0005_auto_20180612_1924'),
        ('crm', '0031_auto_20180612_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Project name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modification', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('default_template_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoUserExtension.TemplateSet', verbose_name='Default Template Set')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='db_project_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('project_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='db_rel_project_staff', to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectLinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Project Link Type',
                'verbose_name_plural': 'Project Link Type',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('is_done', models.BooleanField(verbose_name='Status represents project is done')),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Status',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ProjectStatus', verbose_name='Project Status'),
        ),
    ]
