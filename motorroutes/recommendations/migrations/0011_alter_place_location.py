# Generated by Django 3.2 on 2021-05-26 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
        ('recommendations', '0010_auto_20210526_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.location'),
        ),
    ]
