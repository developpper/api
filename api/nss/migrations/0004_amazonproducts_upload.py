# Generated by Django 3.2.9 on 2022-09-26 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nss', '0003_alter_amazonproducts_amazon_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonproducts',
            name='upload',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]