# Generated by Django 3.2.12 on 2022-03-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_bookname_issue_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='studentid',
            field=models.IntegerField(null=True),
        ),
    ]
