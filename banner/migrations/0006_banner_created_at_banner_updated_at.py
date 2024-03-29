# Generated by Django 4.1.7 on 2023-04-02 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0005_remove_banner_unique_active_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last updated at'),
        ),
    ]
