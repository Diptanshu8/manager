# Generated by Django 2.0.1 on 2018-01-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0003_remove_activity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='data',
            field=models.TextField(default=''),
        ),
    ]
