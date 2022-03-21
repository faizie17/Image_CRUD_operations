# Generated by Django 4.0.2 on 2022-02-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productname', models.CharField(max_length=100)),
                ('productprice', models.CharField(max_length=200)),
                ('productquantity', models.CharField(max_length=200)),
                ('productimage', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
