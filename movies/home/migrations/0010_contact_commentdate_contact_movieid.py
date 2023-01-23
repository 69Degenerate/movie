# Generated by Django 4.0.3 on 2023-01-21 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='commentdate',
            field=models.CharField(blank=True, default='H%:M% D%:M%:2023', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='movieid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='home.moviesinfo'),
        ),
    ]