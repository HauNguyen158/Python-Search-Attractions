# Generated by Django 3.2.3 on 2021-05-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210519_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaiDat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(max_length=200)),
                ('botname', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]