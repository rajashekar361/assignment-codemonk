# Generated by Django 5.0.6 on 2024-06-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('createdAt', models.DateField()),
                ('modifiedAt', models.DateField()),
            ],
        ),
    ]