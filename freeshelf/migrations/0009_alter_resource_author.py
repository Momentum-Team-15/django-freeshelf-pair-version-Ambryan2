# Generated by Django 4.1.2 on 2022-10-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0008_alter_resource_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]
