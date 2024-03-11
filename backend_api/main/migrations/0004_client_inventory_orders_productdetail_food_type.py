# Generated by Django 5.0.2 on 2024-03-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_food_races'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.TextField(null=True)),
                ('name', models.TextField(null=True)),
                ('surname', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('telephone_number', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inventory_ID', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(null=True)),
                ('date', models.TextField(null=True)),
                ('customer_id', models.TextField(null=True)),
                ('product_id', models.TextField(null=True)),
                ('quantity', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.CharField(max_length=200)),
                ('order_id', models.TextField(null=True)),
                ('product_id', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('unit_price', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='Type',
            field=models.TextField(null=True),
        ),
    ]