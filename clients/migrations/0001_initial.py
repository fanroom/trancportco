# Generated by Django 3.0.5 on 2020-05-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('patronymic', models.CharField(max_length=20)),
                ('name_of_organization', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('FZ', 'Individuals'), ('UR', 'Entities')], max_length=2)),
            ],
        ),
    ]
