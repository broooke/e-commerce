# Generated by Django 3.1.5 on 2021-01-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField()),
            ],
        ),
    ]