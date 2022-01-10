# Generated by Django 4.0.1 on 2022-01-10 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigpixel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixeltrackingcode',
            name='tracking_code_status',
            field=models.CharField(default='unreachable', max_length=30),
        ),
        migrations.CreateModel(
            name='PixelTrackingCodeSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('website', models.URLField(max_length=55, unique=True)),
                ('integration_status', models.CharField(choices=[('active', 'Active'), ('invalid', 'Invalid'), ('unreachable', 'Unreachable')], default='unreachable', max_length=30)),
                ('tracking_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bigpixel.pixeltrackingcode')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]