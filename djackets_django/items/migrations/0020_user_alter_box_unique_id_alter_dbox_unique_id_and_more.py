# Generated by Django 4.2.7 on 2023-12-11 10:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0019_alter_box_unique_id_alter_dbox_unique_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_ID', models.CharField(blank=True, default=uuid.UUID('a09ceb25-89ed-49d2-aabb-b9308835d516'), max_length=100, null=True, unique=True)),
                ('nfc_number', models.CharField(blank=True, default=uuid.UUID('e4e328f8-6cab-4be6-988f-33bd0a49f522'), max_length=100, null=True, unique=True)),
                ('name', models.TextField(help_text='Required', verbose_name='title')),
                ('products_taken', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='box',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('20615e25-07ab-4977-873c-2e96af273ed3'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dbox',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('a22bbafb-1e0e-4615-8d97-4fb4a3b5676e'), max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_ID',
            field=models.CharField(blank=True, default=uuid.UUID('55ce2f50-6542-411e-b40e-b193038c8ab1'), max_length=100, null=True, unique=True),
        ),
    ]
