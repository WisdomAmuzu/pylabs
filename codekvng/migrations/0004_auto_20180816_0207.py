# Generated by Django 2.1rc1 on 2018-08-16 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codekvng', '0003_remove_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='date',
        ),
    ]
