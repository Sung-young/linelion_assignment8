# Generated by Django 5.0.4 on 2024-04-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.tag'),
        ),
    ]
