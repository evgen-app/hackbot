# Generated by Django 4.0.3 on 2022-03-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_models', '0010_auto_20220320_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
