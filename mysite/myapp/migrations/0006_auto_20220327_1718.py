# Generated by Django 3.2.12 on 2022-03-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220327_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issued',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='issue',
            name='submitdate',
            field=models.DateField(null=True),
        ),
    ]