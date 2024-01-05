# Generated by Django 4.2.7 on 2024-01-05 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0024_alter_box_unique_id_alter_dbox_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('a3a6af53-c514-4050-ad59-7420b5e83f4c'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('c893fc21-c9b3-4b43-920a-a9499f4f4ba5'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('a686fd7d-38ae-4689-a8fa-c04063ddb36b'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nfc_number',
            field=models.CharField(blank=True, default=uuid.UUID('9d6cd3d2-7258-460b-8f99-fbb0e63fb7d0'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('3d68ad27-51d9-40de-8141-59a2762656de'), max_length=100, null=True, unique=True),
        ),
    ]
