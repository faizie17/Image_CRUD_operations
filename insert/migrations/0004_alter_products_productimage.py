# Generated by Django 4.0.2 on 2022-03-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insert', '0003_alter_products_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
