# Generated by Django 3.2.3 on 2021-05-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoanhThu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('month', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='soluongkhach',
            name='moth',
        ),
        migrations.AddField(
            model_name='soluongkhach',
            name='month',
            field=models.DateField(default=-2006),
            preserve_default=False,
        ),
    ]
