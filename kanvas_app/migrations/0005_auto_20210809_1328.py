# Generated by Django 3.2.6 on 2021-08-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanvas_app', '0004_alter_activity_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='activity',
        ),
        migrations.AddField(
            model_name='submission',
            name='activity',
            field=models.ManyToManyField(to='kanvas_app.Activity'),
        ),
    ]
