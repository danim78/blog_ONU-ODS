# Generated by Django 3.2.9 on 2021-12-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20211220_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='titulo',
            field=models.CharField(max_length=45),
        ),
    ]
