# Generated by Django 3.0.4 on 2020-04-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True),
        ),
    ]
