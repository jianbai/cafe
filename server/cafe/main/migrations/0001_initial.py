# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.CharField(max_length=100)),
                ('user2', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('user1showedUp', models.BooleanField()),
                ('user2showedUp', models.BooleanField()),
                ('location', models.ForeignKey(to='main.Location')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(verbose_name=b'user creation date')),
                ('signedIn', models.BooleanField()),
                ('inPool', models.BooleanField()),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('totalMatches', models.IntegerField()),
                ('missedMatches', models.IntegerField()),
            ],
        ),
    ]
