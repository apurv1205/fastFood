import csv
import json,os
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
	mydict["model"]="foodSite.Restaurant"
	mydict["pk"]=a
	a=a+1
#print(row[0])

	field_dict={}
	field_dict["rest_id"]=int(row[0])
	#field_dict["rest_id"]=int(filename[1:len(filename)-3])
	field_dict["name"]=row[1]
	field_dict["address"]=row[2]
	field_dict["contact"]=contact
	contact=contact+5
	field_dict["passwd"]="asket"
	field_dict["website"]=row[3]
	field_dict["rating"]=float(row[4])

	#r=random(6)
	#field_dict["cuisine"]=clist[r]
	mydict["fields"]=field_dict
	mylist.append(mydict)
f.close()

f1=open("res.json","wb")
json.dump(mylist,f1)