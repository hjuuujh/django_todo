# Generated by Django 3.2.5 on 2021-07-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
    ]
