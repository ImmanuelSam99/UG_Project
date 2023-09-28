# Generated by Django 2.2.6 on 2019-11-11 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking_system', '0006_auto_20191024_1848'),
        ('sales', '0005_remove_invoice_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bank_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_detail_payments', to='banking_system.Bank'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Check', 'Check')], default='Cash', max_length=100),
        ),
    ]