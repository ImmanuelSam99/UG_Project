# Generated by Django 2.2.6 on 2019-11-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_purchaseditem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='notify_qty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True),
        ),
    ]
