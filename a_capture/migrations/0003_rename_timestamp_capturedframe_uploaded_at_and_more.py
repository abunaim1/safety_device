# Generated by Django 5.0.6 on 2025-01-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_capture', '0002_remove_capturedframe_image_capturedframe_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capturedframe',
            old_name='timestamp',
            new_name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='capturedframe',
            name='media',
            field=models.ImageField(upload_to='frames/'),
        ),
    ]
