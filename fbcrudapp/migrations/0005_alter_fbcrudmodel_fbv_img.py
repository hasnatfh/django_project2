# Generated by Django 4.1.4 on 2022-12-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbcrudapp', '0004_rename_fbvimg_fbcrudmodel_fbv_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbcrudmodel',
            name='fbv_img',
            field=models.ImageField(blank=True, null=True, upload_to='fbv-img/'),
        ),
    ]