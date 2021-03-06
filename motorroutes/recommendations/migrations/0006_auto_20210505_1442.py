# Generated by Django 3.2 on 2021-05-05 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0005_alter_onlinelink_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlinelink',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='onlinelink',
            old_name='gallery_id',
            new_name='gallery',
        ),
        migrations.RenameField(
            model_name='onlinelink',
            old_name='google_id',
            new_name='google',
        ),
        migrations.RenameField(
            model_name='onlinelink',
            old_name='user_id',
            new_name='userprofile',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='user_id',
            new_name='userprofile',
        ),
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='navigation.location'),
            preserve_default=False,
        ),
    ]
