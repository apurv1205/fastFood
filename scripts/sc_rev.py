import csv
import json,os
import random
mylist=[]
#clist=["North Indian","Italian","Continental","Chinese","Mexican","South Indian"]
b=1
l1=[]

for filename in os.listdir("/home/asket/Desktop/DBMS/reviews"):
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
			mydict["model"]="foodSite.Reviews"
			mydict["pk"]=b
			b=b+1
		#print(row[0])
			if (row[1],row[3]) in l1:
				continue
			
			l1.append((row[1],row[3]))
			#l2.append(row[3])		
			field_dict={}
			#field_dict["food_id"]=row[0]
			field_dict["rest_id"]=int(filename[0:len(filename)-4])
			field_dict["user_name"]=row[1]
			field_dict["rating"]=float(row[2])
			field_dict["review"]=row[3]
			field_dict["votes"]=random.randint(100,500)
			mydict["fields"]=field_dict
			mylist.append(mydict)
		f.close()

	f1=open("revi.json","wb")
	json.dump(mylist,f1)