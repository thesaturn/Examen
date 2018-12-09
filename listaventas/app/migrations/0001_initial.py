# Generated by Django 2.1.2 on 2018-11-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('anio', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=30)),
                ('nropuertas', models.PositiveIntegerField(max_length=30)),
                ('descripcion', models.TextField(max_length=200)),
                ('fechapub', models.DateTimeField()),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
    ]