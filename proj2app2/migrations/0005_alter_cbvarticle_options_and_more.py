# Generated by Django 4.1.4 on 2022-12-19 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj2app2', '0004_cbvcontactinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cbvarticle',
            options={'verbose_name_plural': 'Cbv Articles'},
        ),
        migrations.AlterModelOptions(
            name='cbvcontactinfo',
            options={'verbose_name_plural': 'Cbv Contact'},
        ),
    ]
