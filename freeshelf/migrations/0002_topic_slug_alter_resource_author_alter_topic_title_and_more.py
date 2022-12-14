# Generated by Django 4.1.2 on 2022-10-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
