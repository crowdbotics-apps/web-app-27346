# Generated by Django 2.2.20 on 2021-05-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_app_plan_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='framework',
            field=models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], max_length=20, verbose_name='Framework'),
        ),
        migrations.AlterField(
            model_name='app',
            name='type',
            field=models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=10, verbose_name='Type'),
        ),
    ]
