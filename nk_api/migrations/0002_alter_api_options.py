# Generated by Django 4.2.13 on 2024-05-15 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nk_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api',
            options={'managed': True, 'ordering': ('nombre',)},
        ),
    ]