# Generated by Django 4.2.7 on 2023-11-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corner_ai', '0003_alter_cornerimage_picture_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerimage',
            name='picture_id',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
