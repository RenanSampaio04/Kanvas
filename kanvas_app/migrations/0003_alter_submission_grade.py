# Generated by Django 3.2.6 on 2021-08-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanvas_app', '0002_auto_20210809_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]