# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'/images')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forename', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='api.Question', db_column=b'Question_id'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='api.User', db_column=b'User_id'),
        ),
    ]
