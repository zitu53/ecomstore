# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, help_text='unique value for product page url')),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(verbose_name='Meta Keywords', max_length=255, help_text='Comma delimited set of SEO keywords for meta tag')),
                ('meta_description', models.CharField(verbose_name='Meta Description', max_length=255, help_text='Content for description meta tag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True, help_text='unique value for product page url', max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(max_digits=9, default=0.0, decimal_places=2, blank=True)),
                ('image', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=255, help_text='Comma delimited set of SEO keywords for meta tag')),
                ('meta_description', models.CharField(max_length=255, help_text='Content for description meta tag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
    ]
