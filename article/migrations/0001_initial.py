# Generated by Django 2.2.2 on 2019-09-21 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField()),
                ('article_number', models.CharField(max_length=10)),
                ('workflow_state', models.CharField(choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published'), ('retired', 'Retired'), ('outdated', 'Outdated')], max_length=20)),
                ('article_body', models.CharField(max_length=2000)),
                ('article_category', models.CharField(choices=[('1', 'Tower'), ('2', 'Insurance'), ('3', 'Sales')], max_length=1)),
                ('disable_commenting', models.BooleanField(default=True)),
                ('topic', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parentArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
        ),
    ]
