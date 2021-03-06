# Generated by Django 3.2.9 on 2021-12-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=30)),
                ('contraseña', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfil')),
            ],
        ),
    ]
