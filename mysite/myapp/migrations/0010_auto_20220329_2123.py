# Generated by Django 3.2.12 on 2022-03-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_issue_studentid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submit',
            old_name='bookname',
            new_name='isbn',
        ),
        migrations.AddField(
            model_name='submit',
            name='studentid',
            field=models.IntegerField(null=True),
        ),
    ]
