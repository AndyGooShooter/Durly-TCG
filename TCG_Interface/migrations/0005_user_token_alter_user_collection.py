# Generated by Django 4.0.5 on 2022-12-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCG_Interface', '0004_alter_user_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='collection',
            field=models.JSONField(default=''),
        ),
    ]
