# Generated by Django 2.2 on 2021-04-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vendor_code',
        ),
        migrations.AddField(
            model_name='product',
            name='vendor_code_old',
            field=models.IntegerField(default=0, verbose_name='Vendor Code'),
            preserve_default=False,
        ),
    ]
