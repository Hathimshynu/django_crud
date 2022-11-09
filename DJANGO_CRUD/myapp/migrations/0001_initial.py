# Generated by Django 4.1.1 on 2022-10-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('job', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
