# Generated by Django 4.1 on 2022-10-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_moviesinfo_cast_moviesinfo_desc_moviesinfo_gerne_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesinfo',
            name='link1080p',
            field=models.TextField(blank=True, default='#', null=True),
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='link480p',
            field=models.TextField(blank=True, default='#', null=True),
        ),
        migrations.AlterField(
            model_name='moviesinfo',
            name='link720p',
            field=models.TextField(blank=True, default='#', null=True),
        ),
    ]
