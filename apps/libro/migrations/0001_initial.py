# Generated by Django 3.0.4 on 2020-03-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre autor')),
                ('last_name', models.CharField(max_length=220, verbose_name='Apellido autor')),
                ('nationality', models.CharField(max_length=100, verbose_name='Nacionalidad')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Biografía')),
                ('state', models.BooleanField(default=True, verbose_name='Auto activo / No activo')),
            ],
        ),
    ]
