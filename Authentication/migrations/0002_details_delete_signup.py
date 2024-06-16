# Generated by Django 5.0.6 on 2024-06-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Pwd', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('createdAt', models.DateField()),
                ('modifiedAt', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
