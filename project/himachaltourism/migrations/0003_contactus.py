# Generated by Django 3.0.7 on 2020-12-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himachaltourism', '0002_ims'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]