# Generated by Django 2.1.5 on 2019-01-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20190123_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usagehead', models.CharField(default='Usage', max_length=200)),
                ('usagebody', models.TextField(default=' ')),
            ],
        ),
    ]
