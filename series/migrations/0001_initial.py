# Generated by Django 4.2.11 on 2024-03-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('pic_img', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=20)),
                ('chapters_number', models.IntegerField(default=0)),
                ('donwloaded_times', models.IntegerField(default=0)),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
