# Generated by Django 3.2.12 on 2022-03-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220327_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='rollno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submit',
            name='rollno',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
