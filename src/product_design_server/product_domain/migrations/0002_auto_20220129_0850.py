# Generated by Django 3.2.11 on 2022-01-29 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandbagDetail',
            fields=[
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000)),
                ('description', models.TextField()),
                ('metadata', models.JSONField(default=dict)),
                ('product_type', models.TextField(default='ACCESSORIES')),
                (
                    'product',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_domain.product'),
                ),
            ],
            options={'db_table': 'pd_handbag_detail',},
        ),
        migrations.AddIndex(
            model_name='handbagdetail',
            index=models.Index(fields=['name', 'product_type'], name='pd_handbag__name_fe8748_idx'),
        ),
        migrations.AlterUniqueTogether(name='handbagdetail', unique_together={('name', 'product_type')},),
    ]
