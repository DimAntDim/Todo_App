# Generated by Django 3.2.4 on 2021-06-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20210619_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creator',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
