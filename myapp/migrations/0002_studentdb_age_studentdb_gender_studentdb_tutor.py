# Generated by Django 5.1.3 on 2024-11-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdb',
            name='AGE',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentdb',
            name='GENDER',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentdb',
            name='TUTOR',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
