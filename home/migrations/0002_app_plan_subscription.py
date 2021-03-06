# Generated by Django 2.2.20 on 2021-05-24 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('WEB', 'Web'), ('MOBILE', 'Mobile')], max_length=10, verbose_name='Type')),
                ('framework', models.CharField(choices=[('DJANGO', 'Django'), ('REACT_NATIVE', 'React Native')], max_length=20, verbose_name='Framework')),
                ('domain_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Domain Name')),
                ('screenshot', models.URLField(blank=True, null=True, verbose_name='Screenshot')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='home.App')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='home.Plan')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
