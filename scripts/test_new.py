import csv
import json,os
from random import randint

def min(a,b):
	if a>b:
		return b
	else:
		return a


mylist1=[]

b=1
c=1

cat=["Breakfast","Lunch","Dinner"]
for filename in os.listdir("/home/asket/Desktop/DBMS/menu"):
	if filename.endswith(".csv"):
		
		f=open(filename,"rb")
		reader=csv.reader(f)
		a=0
		#contact=900784657
		for row in reader:
			if a==0:
				a=1
				continue
			mydict={}
			mydict["model"]="foodSite.FoodItems"
			mydict["pk"]=b
			b=b+1
		#print(row[0])
		
			field_dict={}
			
			
			field_dict["rest"]=int(filename[0:len(filename)-4])
			
			field_dict["food_id"]=c
			c=c+1
			field_dict["name"]=row[1][0:min(49,len(row[1]))]
			field_dict["price"]=row[2]
			r=randint(0,5)
			field_dict["cuisine"]=clist[r]
			r=randint(0,2)
			field_dict["category"]=cat[r]
			field_dict["photo"]="aaaaa"
			mydict["fields"]=field_dict
			mylist1.append(mydict)
			
		f.close()

f1=open("menu.json","wb")
json.dump(mylist1,f1)
f1.close()
