import csv
import json,os
from django.contrib.auth.hashers import make_password, HASHERS
mylist=[]
#clist=["North Indian","Italian","Continental","Chinese","Mexican","South Indian"]


f=open("final_res.csv","rb")
reader=csv.reader(f)
a=0
contact=900784657
for row in reader:
	if a==0:
		a=1
		continue
	mydict={}
	mydict["model"]="auth.User"
	mydict["pk"]=a
	a=a+1
#print(row[0])

	field_dict={}
	field_dict["first_name"]=row[1]
	#field_dict["rest_id"]=int(filename[1:len(filename)-3])
	field_dict["last_name"]="R"
	#field_dict["address"]=row[2]
	field_dict["username"]=str(contact)
	contact=contact+5
	p=make_password("asket",str(a))
	field_dict["password"]=p
	
	#r=random(6)
	#field_dict["cuisine"]=clist[r]
	mydict["fields"]=field_dict
	mylist.append(mydict)
f.close()

f1=open("usr.json","wb")
json.dump(mylist,f1)