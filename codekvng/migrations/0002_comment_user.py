# Generated by Django 2.1rc1 on 2018-08-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codekvng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='Codekvng', max_length=100),
            preserve_default=False,
        ),
    ]
