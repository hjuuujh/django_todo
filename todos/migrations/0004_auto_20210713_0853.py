# Generated by Django 3.2.5 on 2021-07-12 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_todo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='contents',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]