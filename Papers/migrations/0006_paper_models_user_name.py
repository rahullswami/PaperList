# Generated by Django 4.2.5 on 2024-09-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Papers', '0005_paper_models_paper_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper_models',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
