# Generated by Django 4.2.4 on 2023-09-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course', models.CharField(max_length=30)),
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
