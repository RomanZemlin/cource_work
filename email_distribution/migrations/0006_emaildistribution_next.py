# Generated by Django 4.2.5 on 2023-10-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_distribution', '0005_rename_status_logs_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaildistribution',
            name='next',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата следующей попытки'),
        ),
    ]