# Generated by Django 3.2.9 on 2021-12-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='post/'),
        ),
    ]
