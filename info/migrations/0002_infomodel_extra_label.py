# Generated by Django 3.0 on 2024-04-19 14:02

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomodel',
            name='extra_label',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]