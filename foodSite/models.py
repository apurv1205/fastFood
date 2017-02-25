from __future__ import unicode_literals
from django.db import models


class Customer(models.Model):
	user_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	passwd=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	cantact=models.CharField(max_length=20,null=True)

class Restaurant(models.Model):
	rest_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	passwd=models.CharField(max_length=100,null=True)
	contact=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	address=models.TextField(null=True)
	rating=models.FloatField(null=True)

class FoodItems(models.Model):
	food_id=models.IntegerField(null=True)
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=50,null=True)
	contact=models.CharField(max_length=20,null=True)
	cuisine=models.CharField(max_length=10,null=True)
	category=models.CharField(max_length=20,null=True)

class Reviews(models.Model):
	user_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
	rest_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
	votes=models.IntegerField(null=True)
	rating=models.FloatField(null=True)
	review=models.TextField(null=True)


class CurrentOrders(models.Model):
	address=models.CharField(max_length=150,null=True)
	order_id=models.IntegerField(null=True)
	user_id=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.PROTECT)
	status=models.CharField(max_length=10,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)

	def place_order(self):
		self.order_timestamp=timezone.now()
		self.save()


class OrderDetails(models.Model):
	order_id=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	food_id=models.ForeignKey(FoodItems,null=True,on_delete=models.PROTECT)
	quantity=models.IntegerField(null=True)


class OrderHistory(models.Model):
	order_id=models.IntegerField(null=True)
	user_id=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
	rating=models.FloatField(null=True)