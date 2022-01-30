# Generated by Django 3.2.11 on 2022-01-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_domain', '0003_alter_product_description'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='handbagdetail',
            name='pd_handbag__name_fe8748_idx',
        ),
        migrations.AddField(
            model_name='handbagdetail',
            name='type',
            field=models.TextField(default='HANDBAGS'),
        ),
        migrations.AlterUniqueTogether(
            name='handbagdetail',
            unique_together={('name', 'type')},
        ),
        migrations.AddIndex(
            model_name='handbagdetail',
            index=models.Index(fields=['name', 'type'], name='pd_handbag__name_97b834_idx'),
        ),
        migrations.RemoveField(
            model_name='handbagdetail',
            name='product_type',
        ),
    ]