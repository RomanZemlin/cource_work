# Generated by Django 4.2.5 on 2023-10-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_distribution', '0010_emaildistribution_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildistribution',
            name='period',
            field=models.CharField(choices=[('1', 'Раз в день'), ('2', 'Раз в неделю'), ('3', 'Раз в месяц')], default='1', max_length=255, verbose_name='Период рассылки'),
        ),
    ]
