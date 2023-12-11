# Generated by Django 4.2.7 on 2023-12-07 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_alter_box_unique_id_alter_dbox_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('eacb75df-ccee-476a-8e22-fce24327be75'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('502bb667-e39b-494e-9bcc-41a961a5efa4'), max_length=100, null=True, unique=True),
        ),
    ]
