# Generated by Django 5.0.2 on 2024-03-11 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_species_name_species_species_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeciesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Species', models.CharField(max_length=200)),
                ('name', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='species',
            name='Species_ID',
        ),
        migrations.RemoveField(
            model_name='species',
            name='species_Name',
        ),
        migrations.AddField(
            model_name='species',
            name='tipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product', to='main.speciescategory'),
        ),
    ]