# Generated by Django 3.0.3 on 2020-02-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_remove_customuser_operators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
