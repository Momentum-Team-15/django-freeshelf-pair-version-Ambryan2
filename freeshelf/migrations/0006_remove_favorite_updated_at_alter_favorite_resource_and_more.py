# Generated by Django 4.1.2 on 2022-10-26 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0005_remove_resource_favorite_alter_resource_topic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='freeshelf.resource'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
