# Generated by Django 4.1.2 on 2022-10-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
