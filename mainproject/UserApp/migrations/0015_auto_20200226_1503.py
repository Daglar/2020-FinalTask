# Generated by Django 3.0.3 on 2020-02-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0014_auto_20200225_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserregistration',
            name='shop_link',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
