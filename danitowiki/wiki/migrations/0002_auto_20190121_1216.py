# Generated by Django 2.1.5 on 2019-01-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='languagecont',
            name='figure',
            field=models.CharField(default='guido', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='languagecont',
            name='figureinfo',
            field=models.TextField(default='guido info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='languagecont',
            name='information',
            field=models.TextField(default='info'),
            preserve_default=False,
        ),
    ]
