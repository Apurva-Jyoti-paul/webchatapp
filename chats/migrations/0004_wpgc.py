# Generated by Django 3.1.7 on 2021-02-22 13:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0003_auto_20210222_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='wpgc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='New_group', max_length=100)),
                ('creatorid', models.IntegerField(default=1)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
