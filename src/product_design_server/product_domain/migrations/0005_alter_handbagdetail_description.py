# Generated by Django 3.2.11 on 2022-01-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_domain', '0004_auto_20220130_0913'),
    ]

    operations = [
        migrations.AlterField(model_name='handbagdetail', name='description', field=models.TextField(null=True),),
    ]
