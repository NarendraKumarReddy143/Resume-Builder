# Generated by Django 4.1.7 on 2023-06-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newresume', '0002_signin'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mail', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
    ]