# Generated by Django 3.0.3 on 2020-03-06 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200304_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category_count',
        ),
    ]
