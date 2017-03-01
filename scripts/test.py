import csv
import json,os
mylist=[]
clist=["North Indian","Italian","Continental","Chinese","Mexican","South Indian"]
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
			mydict["pk"]=a
			a=a+1
		#print(row[0])
		
			field_dict={}
			#field_dict["food_id"]=row[0]
			field_dict["rest_id"]=int(filename[1:len(filename)-3])
			field_dict["name"]=row[1]
			field_dict["price"]=row[2]
			r=random(6)
			field_dict["cuisine"]=clist[r]
			mydict["fields"]=field_dict
			mylist.append(mydict)
			close(f)

	f1=open("menu.json","wb")
	json.dump(mylist,f1)