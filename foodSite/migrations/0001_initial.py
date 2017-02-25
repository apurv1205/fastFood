# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('order_timestamp', models.DateTimeField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('cantact', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('photo', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=20, null=True)),
                ('cuisine', models.CharField(max_length=10, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('food_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='foodSite.FoodItems')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='foodSite.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('order_timestamp', models.DateTimeField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('rating', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('rest_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('rating', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(null=True)),
                ('rating', models.FloatField(null=True)),
                ('review', models.TextField(null=True)),
                ('rest_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodSite.Restaurant')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodSite.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='rest_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodSite.Restaurant'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodSite.Customer'),
        ),
        migrations.AddField(
            model_name='fooditems',
            name='rest_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodSite.Restaurant'),
        ),
        migrations.AddField(
            model_name='currentorders',
            name='rest_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='foodSite.Restaurant'),
        ),
        migrations.AddField(
            model_name='currentorders',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='foodSite.Customer'),
        ),
    ]