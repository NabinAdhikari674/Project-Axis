# Generated by Django 3.0.8 on 2020-08-08 17:15

import autoslug.fields
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
            name='postReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.BigIntegerField()),
                ('reaction', models.IntegerField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='postComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.BigIntegerField()),
                ('parentId', models.IntegerField()),
                ('comment', models.TextField()),
                ('popularity', models.IntegerField(default=0)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('commentAuthor', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTitle', models.CharField(max_length=200)),
                ('postSlug', autoslug.fields.AutoSlugField(editable=False, populate_from='postTitle', unique=True)),
                ('status', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('category', models.IntegerField(default=0)),
                ('axisStatus', models.IntegerField(default=0)),
                ('postLevel', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('startDate', models.DateTimeField(blank=True, null=True)),
                ('endDate', models.DateTimeField(blank=True, null=True)),
                ('popularity', models.BigIntegerField(default=0)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('postAuthor', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['popularity'],
            },
        ),
        migrations.CreateModel(
            name='commentReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentId', models.IntegerField()),
                ('reaction', models.IntegerField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
