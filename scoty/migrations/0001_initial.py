# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SenderName', models.CharField(max_length=30)),
                ('SenderAddress', models.CharField(max_length=30)),
                ('RecieverName', models.CharField(max_length=30)),
                ('RecieverAddress', models.CharField(max_length=30)),
                ('referenceID', models.CharField(max_length=30)),
                ('GoodsareFrom', models.CharField(max_length=30)),
                ('GoodsTo', models.CharField(max_length=30)),
                ('DepatureDate', models.CharField(max_length=30)),
                ('Depaturetime', models.CharField(max_length=30)),
                ('ArrivalDate', models.CharField(max_length=30)),
                ('ArrivalTime', models.CharField(max_length=30)),
                ('GoodsDescription', models.TextField(max_length=50)),
                ('Status', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrackForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReferenceId', models.CharField(max_length=30)),
                ('Sender', models.CharField(max_length=30)),
                ('Reciever', models.CharField(max_length=30)),
                ('newform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoty.NewForm')),
            ],
        ),
    ]
