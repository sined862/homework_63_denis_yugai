# Generated by Django 4.1.2 on 2022-10-27 07:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_text'),
        ('accounts', '0005_account_liked_posts_account_subscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
