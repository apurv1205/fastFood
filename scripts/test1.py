import csv
import json,os
from random import randint
mylist1=[]
mylist2=[]
mylist3=[]
mylist4=[]
b=1
clist=["North Indian","Italian","Continental","Chinese","Mexican","South Indian"]
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
			field_dict["food_id"]=int(row[0])
			field_dict["rest"]=int(filename[0:len(filename)-4])

			field_dict["name"]=row[1]
			field_dict["price"]=row[2]
			r=randint(0,5)
			field_dict["cuisine"]=clist[r]
			r=randint(0,2)
			field_dict["category"]=cat[r]
			field_dict["photo"]="aaaaa"
			mydict["fields"]=field_dict
			if b%4==0:
				mylist1.append(mydict)
			if b%4==1:
				mylist2.append(mydict)
			if b%3==2:
				mylist3.append(mydict)
			if b%4==3:
				mylist4.append(mydict)
		f.close()

f1=open("menu1.json","wb")
json.dump(mylist1,f1)
f1.close()
f1=open("menu2.json","wb")
json.dump(mylist2,f1)
f1.close()
f1=open("menu3.json","wb")
json.dump(mylist3,f1)
f1.close()
f1=open("menu4.json","wb")
json.dump(mylist4,f1)
f1.close()