# Generated by Django 4.2.7 on 2024-01-08 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0028_remove_user_unique_id_alter_box_unique_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nfc_number',
        ),
        migrations.AddField(
            model_name='user',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('77e7c3ea-f9cc-481f-8558-33a6721975a7'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('7f0067d4-ff96-4ad8-8104-eb19439c3f5a'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('3bc01fb0-51a9-45f7-b458-7635f5124adc'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(help_text='Required', verbose_name='title'),
        ),
    ]
