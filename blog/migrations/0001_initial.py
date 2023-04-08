# Generated by Django 3.2.18 on 2023-04-08 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentFeeling',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
