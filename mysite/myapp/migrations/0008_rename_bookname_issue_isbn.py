# Generated by Django 3.2.12 on 2022-03-28 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220327_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='bookname',
            new_name='isbn',
        ),
    ]
