# Generated by Django 5.0.2 on 2024-03-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Species_ID', models.TextField(null=True)),
                ('Species_Name', models.TextField(null=True)),
            ],
        ),
    ]
