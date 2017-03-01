from foodSite.models import *
import time
import json
from datetime import datetime

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
    return strTimeProp(start, end, '%Y-%m-%d %I:%M %p', prop)







mylist=[]
b=1

cust = Customer.objects.all()
food_items=FoodItems.objects.all()
for customer in cust:
	print customer.user_id
        for fi in food_items:
		k=random.randint(0,6)
		if k==0:
			mydict={}
			mydict["model"]="foodSite.OrderHistory"
			mydict["pk"]=b
			b+=1
			field_dict={}
			field_dict["food"]=fi.food_id
			field_dict["rest"]=fi.rest.rest_id
			field_dict["quantity"]=random.randint(1,3)
			field_dict["order_id"]=b
			field_dict["user"]=customer.user_id
			field_dict["status"]="Delivered"
			field_dict["order_timestamp"]=str(datetime.now())
			field_dict["amount"]=random.randint(200,1000)
			field_dict["rating"]=random.uniform(0,5)
			mydict["fields"]=field_dict
			mylist.append(mydict)


f=open("history.json","wb")
json.dump(mylist,f)
f.close()

