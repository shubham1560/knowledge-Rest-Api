# Generated by Django 2.2.2 on 2019-09-21 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190921_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='parent_article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
        ),
    ]
