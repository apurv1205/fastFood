from __future__ import unicode_literals
from django.db import models
import random
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
	user_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	passwd=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	contact=models.CharField(max_length=20,null=True)

	def __str__(self):
    		return self.name.encode('utf-8')

class Restaurant(models.Model):
	rest_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	passwd=models.CharField(max_length=100,null=True)
	contact=models.CharField(max_length=100,null=True)
	address=models.TextField(null=True)
	email=models.CharField(max_length=100,null=True)
	website=models.CharField(max_length=100,null=True)
	rating=models.FloatField(null=True)

	def __str__(self):
			return self.name.encode('utf-8')

class FoodItems(models.Model):
	food_id=models.IntegerField(primary_key=True)
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=100,null=True)
	cuisine=models.CharField(max_length=20,null=True)
	category=models.CharField(max_length=20,null=True)

	def __str__(self):
			return self.name.encode('utf-8')

class Reviews(models.Model):
	user_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
	rest=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	votes=models.IntegerField(null=True)
	rating=models.FloatField(null=True)
	review=models.TextField(null=True)

class CurrentOrders(models.Model):
	food=models.ForeignKey(FoodItems,null=True,on_delete=models.PROTECT)
	quantity=models.IntegerField(null=True)
	order_id=models.IntegerField(primary_key=True)
	user=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.PROTECT)
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
	address=models.TextField(null=True)

	def place_order(self):
		self.order_timestamp=timezone.now()
		self.save()

class OrderHistory(models.Model):
	food=models.ForeignKey(FoodItems,null=True,on_delete=models.PROTECT)
	quantity=models.IntegerField(null=True)
	order_id=models.IntegerField(null=True)
	user=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
	rating=models.FloatField(null=True)
	