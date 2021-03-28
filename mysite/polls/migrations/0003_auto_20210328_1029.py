# Generated by Django 2.2 on 2021-03-28 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210324_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicewithgoodmarks',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_marks', to='polls.Question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=10, verbose_name='Question Text'),
        ),
    ]
