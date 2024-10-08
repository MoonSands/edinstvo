# Generated by Django 5.0 on 2024-06-08 12:03

import article_feed.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataFromForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True, verbose_name=150)),
                ('phone', models.IntegerField(null=True, verbose_name=11)),
                ('email', models.TextField()),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(default='docs/ИБ.docx', upload_to=article_feed.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='postCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='postContentFilesUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=article_feed.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('preview_image', models.ImageField(default='products/moon.jpg', upload_to=article_feed.models.upload_to)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reportsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('excerpt', models.TextField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('preview_image', models.ImageField(default='posts/moon.jpg', upload_to=article_feed.models.upload_to)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True)),
                ('content', models.JSONField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='article_feed.postcategory')),
            ],
        ),
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(default='reports/%D0%98%D0%91_YdeVSTs.docx', upload_to=article_feed.models.upload_to)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article_feed.reportsgroup')),
            ],
        ),
    ]
