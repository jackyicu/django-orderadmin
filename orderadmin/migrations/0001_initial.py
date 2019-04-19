# Generated by Django 2.1.7 on 2019-04-19 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erp_code', models.CharField(blank=True, max_length=9)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=8)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('installation_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('tag', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Order Date')),
                ('pi_no', models.CharField(max_length=15)),
                ('po_no', models.CharField(blank=True, max_length=15)),
                ('sc_no', models.CharField(blank=True, max_length=15)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(blank=True, max_length=10)),
                ('remarks', models.CharField(blank=True, max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Client')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=None, to='orderadmin.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=None, to='orderadmin.Currency')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=15, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='admin', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bl_date', models.DateField(blank=True, null=True)),
                ('carrier', models.CharField(blank=True, max_length=10)),
                ('tracking_no', models.CharField(blank=True, max_length=20)),
                ('bill_no', models.CharField(blank=True, max_length=10)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Order')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='term',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='orderadmin.PaymentTerm'),
        ),
        migrations.AddField(
            model_name='order',
            name='sales',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Sales'),
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.ForeignKey(on_delete=None, to='orderadmin.Country'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderadmin.Product'),
        ),
    ]
