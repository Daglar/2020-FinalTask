# Generated by Django 3.0.3 on 2020-02-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0012_auto_20200225_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserregistration',
            name='shop_link',
            field=models.URLField(blank=True, default='', max_length=255, null=True),
        ),
    ]
