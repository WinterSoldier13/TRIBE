# Generated by Django 2.2.1 on 2020-01-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='newprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='oldprice',
            field=models.IntegerField(default=0),
        ),
    ]
