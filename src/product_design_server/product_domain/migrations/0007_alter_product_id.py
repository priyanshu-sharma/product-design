# Generated by Django 3.2.11 on 2022-01-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_domain', '0006_alter_handbagdetail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
