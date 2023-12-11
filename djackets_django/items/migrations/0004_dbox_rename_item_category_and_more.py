# Generated by Django 4.2.7 on 2023-12-07 10:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_category_product_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_ID', models.CharField(blank=True, default=uuid.UUID('72ed45b0-ed5e-4ef2-904f-7e08cd06a83c'), max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Item',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='item',
            new_name='category',
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_ID', models.CharField(blank=True, default=uuid.UUID('49ef850e-f703-413c-b3c2-b36834d2ca09'), max_length=100, null=True, unique=True)),
                ('box_num', models.IntegerField()),
                ('isFree', models.BooleanField(default=False)),
                ('dbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.dbox')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='box',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='items.box'),
        ),
    ]
