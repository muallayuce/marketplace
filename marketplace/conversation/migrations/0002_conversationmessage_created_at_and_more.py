# Generated by Django 4.2.3 on 2023-08-02 10:58

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conversation',
            name='members',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
