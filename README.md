# Online food ordering system
> Group project for DBMS lab course in IIT Kharagpur  

## Contributors

1. [Apurv Kumar](https://github.com/apurv1205)
2. [Aniket Choudhary](https://github.com/aniket1743)
2. [Asket Agarwal](https://github.com/asketagarwal)
4. [Rameshwar Bhaskaran](https://github.com/zorroblue)
5. [Shubham Sharma](https://github.com/shubham4060)

You can check out our website : http://fastfood.pythonanywhere.com/

## Requirements

First create a virtual environment and activate it.  
Now , write the following two commands (required for recommendation system)  
```	
$ pip install scipy  	
$ pip install numpy  	
$ pip install csc-pysparse networkx divisi2  
```
	
We used the following project for the recommendation system which uses collaborative filtering :  
https://github.com/ocelma/python-recsys  

Now clone the above repository  
```	
$ git clone https://github.com/ocelma/python-recsys.git  
```
And run the setup.py to install it
```
	$ cd python-recsys  
	$ python setup.py install  
```
Install all other dependencies using :  
```
$ pip install -r requirements.txt  
```
## Usage

To prepare your database and recommendation system :  
In your fastFood directory type the following, make sure the virtual environment is running  
```	
	$ python manage.py migrate  
	$ python manage.py loaddata usr.json  
	$ python manage.py loaddata res.json  
	$ python manage.py loaddata menu.json  
	$ python manage.py loaddata revi.json  
	$ python manage.py loaddata history.json  
	$ python script1.py   
```
Now, finally to run the webserver type :  
```	
$ python manage.py runserver   
```
and go to 127.0.0.1:8000 using preferably chrome browser  
