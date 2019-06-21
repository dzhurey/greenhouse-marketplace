# Generated by Django 2.2.2 on 2019-06-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
