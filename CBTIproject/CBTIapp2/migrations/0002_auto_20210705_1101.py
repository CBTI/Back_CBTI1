# Generated by Django 3.2.5 on 2021-07-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBTIapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbtiapp2_model',
            name='password',
            field=models.CharField(max_length=32, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='cbtiapp2_model',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]