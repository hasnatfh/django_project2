# Generated by Django 4.1.4 on 2022-12-24 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbcrudapp', '0003_alter_fbcrudmodel_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fbcrudmodel',
            old_name='fbvimg',
            new_name='fbv_img',
        ),
    ]