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
	cantact=models.CharField(max_length=20,null=True)

class Restaurant(models.Model):
	rest_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	passwd=models.CharField(max_length=100,null=True)
	contact=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	address=models.TextField(null=True)

	#def __str__(self):
    #	return self.title


class Restaurant(models.Model):
	rest_id=models.IntegerField(primary_key=True)
	website=models.CharField(max_length=100,null=True)
	name=models.CharField(max_length=100,null=True)
	contact=models.CharField(max_length=100,null=True)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	address=models.TextField(null=True)
	rating=models.FloatField(null=True)

class FoodItems(models.Model):
	food_id=models.IntegerField(null=True)
<<<<<<< HEAD
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=50,null=True)
	contact=models.CharField(max_length=20,null=True)
=======
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=100,null=True)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	cuisine=models.CharField(max_length=10,null=True)
	category=models.CharField(max_length=20,null=True)

class Reviews(models.Model):
	user_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
<<<<<<< HEAD
	rest_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
=======
	rest=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	votes=models.IntegerField(null=True)
	rating=models.FloatField(null=True)
	review=models.TextField(null=True)


class CurrentOrders(models.Model):
<<<<<<< HEAD
	address=models.CharField(max_length=150,null=True)
	order_id=models.IntegerField(null=True)
	user_id=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.PROTECT)
=======
	order_id=models.IntegerField(null=True)
	user=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.PROTECT)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	status=models.CharField(max_length=10,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)

	def place_order(self):
		self.order_timestamp=timezone.now()
		self.save()


class OrderDetails(models.Model):
<<<<<<< HEAD
	order_id=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	food_id=models.ForeignKey(FoodItems,null=True,on_delete=models.PROTECT)
=======
	order=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	food=models.ForeignKey(FoodItems,null=True,on_delete=models.PROTECT)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	quantity=models.IntegerField(null=True)


class OrderHistory(models.Model):
	order_id=models.IntegerField(null=True)
<<<<<<< HEAD
	user_id=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	rest_id=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
=======
	user=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	rest=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE)
>>>>>>> 00ad753503eb95e9ea6dd3eb7d4c195a96707f0e
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
	rating=models.FloatField(null=True)