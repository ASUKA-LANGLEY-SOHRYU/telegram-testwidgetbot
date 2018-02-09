# Generated by Django 2.0.2 on 2018-02-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.CharField(max_length=200)),
                ('tg_first_name', models.CharField(max_length=200)),
                ('tg_last_name', models.CharField(max_length=200)),
                ('tg_username', models.CharField(max_length=200)),
                ('tg_photo_url', models.CharField(max_length=200)),
                ('tg_auth_date', models.CharField(max_length=200)),
                ('tg_hash', models.CharField(max_length=200)),
            ],
        ),
    ]
