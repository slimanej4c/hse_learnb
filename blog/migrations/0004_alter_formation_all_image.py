# Generated by Django 4.2.6 on 2023-11-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_formation_all_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation_all',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]