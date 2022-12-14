# Generated by Django 4.1 on 2022-10-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_moviesinfo_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesinfo',
            name='cast',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='desc',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='gerne',
            field=models.CharField(blank=True, default=None, max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='imdb',
            field=models.CharField(blank=True, default=None, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='link1080p',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='link480p',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='link720p',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='rt',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='image',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='release_year',
            field=models.CharField(blank=True, default=None, max_length=122, null=True),
        ),
    ]
