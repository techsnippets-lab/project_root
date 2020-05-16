# Generated by Django 2.0.7 on 2019-12-28 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comments_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
    ]
