# Generated by Django 3.1.7 on 2022-03-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
