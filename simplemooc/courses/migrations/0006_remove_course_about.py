# Generated by Django 3.2.8 on 2021-10-26 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211026_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='about',
        ),
    ]
