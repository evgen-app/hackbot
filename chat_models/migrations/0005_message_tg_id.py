# Generated by Django 3.1.7 on 2022-03-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_models', '0004_auto_20220319_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tg_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]