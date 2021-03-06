# Generated by Django 3.0.6 on 2021-02-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Country_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PhoneNumber',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
