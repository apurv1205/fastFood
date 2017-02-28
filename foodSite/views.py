from foodSite.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib import messages
from foodSite.models import *
import editdistance
from django.views.decorators.csrf import csrf_exempt
from .forms import AddressForm

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            stat = form.cleaned_data['choice_field']
            status="C";
            if str(stat) == "1" : 
                status="C"
                C=Customer(name=form.cleaned_data['first_name'],passwd=form.cleaned_data['password1'],email=form.cleaned_data['email'],contact=str(form.cleaned_data['username']))
                C.save()

            elif str(stat) == "2": 
                status="R"
                R=Restaurant(name=form.cleaned_data['first_name'],passwd=form.cleaned_data['password1'],email=form.cleaned_data['email'],contact=str(form.cleaned_data['username']))
                R.save() 

            user = User.objects.create_user(
            first_name=form.cleaned_data['first_name'],
            last_name=status,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return render(request,
    'registration/success.html',
    {'form': form}
    )
    else:
        form = RegistrationForm()
 
    return render(request,
    'registration/register.html',
    {'form': form}
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',{'user':request.user}
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
@csrf_exempt
@login_required
def home(request):
    menu = FoodItems.objects.all()
    restaurants = Restaurant.objects.all().order_by('name')
    cart = CurrentOrders.objects.all()
    usr=request.user
    crt=[]
    total=0
    curr_rest=Restaurant.objects.all()
    cur_rest=curr_rest[0]
    form = PostForm()
    lst=[]
    for rest in restaurants :
        if usr.username==rest.contact :
            cur_rest=Restaurant.objects.get(pk=rest.rest_id)

    cart1=[]
    for item in cart :
        if item.rest.rest_id==cur_rest.rest_id :
            if item.status=="Added to cart" : cart1.append(item)
            elif item.status=="Cancelled" : cart1.append(item)
            else : 
                fitem=FoodItems.objects.get(pk=item.food.food_id)
                lst.append([fitem.name,item.user.name,item.status,item.quantity,item.amount,item.pk,item.address])

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            C=FoodItems(name=form.cleaned_data['name'],rest=cur_rest,price=form.cleaned_data['price'],photo="ok",cuisine=form.cleaned_data['cuisine'],category=form.cleaned_data['category'])
            C.save()
            form = PostForm()
            message=[]
            message.append("Added new item : ")
            return render_to_response(
    'rest_home.html', { 'form' : form , 'orders' : lst,'user': usr,'message' : message,'item' : C.name}
    )

    else:
        if usr.last_name == "C" :    
            for item in cart :
                customer = Customer.objects.get(pk=item.user.user_id)
                if customer.contact == usr.username and item.status == "Added to cart":
                    fitem=FoodItems.objects.get(pk=item.food.food_id)
                    ritem=Restaurant.objects.get(pk=item.rest.rest_id)
                    total=total+item.quantity*item.amount
                    crt.append([fitem.name,ritem.name,item.amount,item.quantity,item.status,item.pk])
            
            #search by category
            if request.method == 'GET':
                category_output=[]
                search_query = request.GET.get('search_box', None)
                if search_query!=None:
                    for item in menu:
                        a = item.category.lower()
                        b = search_query.lower()
                        if a == b or a in b or b in a or editdistance.eval(a,b)<=3:
                           category_output.append(item)

                search_output=[]
                search_query = request.GET.get('search_box1', None)
                if search_query!=None:
                    for item in menu:
                        a = item.name.lower()
                        b = search_query.lower()
                        if a == b or a in b or b in a or editdistance.eval(a,b)<=3:
                           search_output.append(item)

            return render_to_response(
            'home.html', { 'total' : total,'cart' : crt, 'user': usr, 'menu' : menu, 'restaurants' : restaurants ,'category_output' : category_output , 'search_output' : search_output}
            )
        elif usr.last_name == "R": 
            return render_to_response(
            'rest_home.html', {'form' : form , 'orders' : lst,'user': usr}
            )
        
        else : 
            logout(request)
            return HttpResponseRedirect('/')

def rest_detail(request, pk):
    menu = FoodItems.objects.all()
    rest = Restaurant.objects.get(pk=pk)
    items=[]
    for item in menu:
        if str(item.rest.rest_id) == str(pk) : 
            items.append(item)
    return render(request, 'rest_detail.html', {'items': items , 'rest' : rest })

@csrf_exempt
def change_status(request, pk):
    order = get_object_or_404(CurrentOrders, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            stat = form.cleaned_data['choice_field']
            stats=""
            if str(stat)=='1' : stats='Confirmed'
            elif str(stat)=='2' : stats='Preparing'
            elif str(stat)=='3' : stats='Out for delivery'
            elif str(stat)=='4' : stats='Delivered'
            CurrentOrders.objects.filter(pk=order.pk).update(status=stats)
            order = get_object_or_404(CurrentOrders, pk=pk)
            if str(stat)=='4' : 
                C=OrderHistory(food=order.food,quantity=order.quantity,order_id=order.order_id,user=order.user,rest=order.rest,status=order.status,order_timestamp=order.order_timestamp,amount=order.amount,rating=0.0)
                C.save()
                order.delete()
                stat="Deliverd and deleted from current orders"
        message=[]
        message.append('Order has been updated to ')

        return render(request, 'change_status.html', {'order': order,'form':form,'message':message,'stats':stats})
    else :
        form = StatusForm() 
        return render(request, 'change_status.html', {'order': order,'form':form})

def cart(request, pk):
    item = get_object_or_404(FoodItems, pk=pk)
    customers = Customer.objects.all()
    orders=CurrentOrders.objects.all()
    user=request.user
    menu = FoodItems.objects.all()
    rest = Restaurant.objects.get(pk=item.rest.rest_id)
    items=[]
    for item1 in menu:
        if str(item1.rest.rest_id) == str(rest.pk) : 
            items.append(item1)

    for cust in customers :
        if user.username == cust.contact :
            flag=False
            for thing in orders :
                if thing.user.user_id==cust.user_id and thing.food.food_id == item.food_id and thing.status=="Added to cart":
                    CurrentOrders.objects.filter(pk=thing.pk).update(quantity=thing.quantity + 1)
                    flag=True

            if flag==False :
                C=CurrentOrders(user=cust,rest=item.rest,status="Added to cart",amount=item.price,food=item,quantity=1)
                C.place_order()
    message=[]
    message.append("Item Added to cart")
    return render(request, 'rest_detail.html', {'items': items , 'rest' : rest ,'message' : message ,'item':item})

@login_required
def checkout(request):
    usr=request.user
    crt=[]
    total = 0
    orders = CurrentOrders.objects.all()
    form = AddressForm()
    for item in orders :
        customer = Customer.objects.get(pk=item.user.user_id)
        if customer.contact == usr.username and item.status == "Added to cart":
            fitem=FoodItems.objects.get(pk=item.food.food_id)
            ritem=Restaurant.objects.get(pk=item.rest.rest_id)
            total=total+item.quantity*item.amount
            crt.append([fitem.name,ritem.name,item.amount,item.quantity,item.status])
    if len(crt)==0:
        return HttpResponseRedirect("/home/")
    ordered_cust=None
    customers =  Customer.objects.all()
    for cust in customers:
        if usr.username == cust.contact:
            ordered_cust = cust
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            if ordered_cust != None:
                #filterargs = { 'user' : ordered_cust , 'status' : "Added to cart"}
                CurrentOrders.objects.filter(user_id__exact = ordered_cust.user_id, status__exact = 'Added to cart').update(address = address, status = 'Confirmed')
                return render(request, 'success.html')
        else:
            form = AddressForm()
            return render(request, 'checkout.html', {'cart' : crt, 'total' : total, 'form':form})
    else:
        return render(request, 'checkout.html', {'cart' : crt, 'total' : total, 'form':form})

@login_required
def current_orders(request):
    user = request.user
    ordered_cust=None
    customers =  Customer.objects.all()
    for cust in customers:
        if user.username == cust.contact:
            ordered_cust = cust
    if ordered_cust!=None:
        orders1 = CurrentOrders.objects.filter(user_id__exact = ordered_cust.user_id)
        orders=[]
        ordersNot = CurrentOrders.objects.filter(user_id__exact = ordered_cust.user_id,status="Added to cart")
        for item in orders1 :
            if item not in ordersNot :
                orders.append(item)

    return render(request, 'view_orders.html',{'orders':orders, 'user' : user})

@login_required
def order_history_user(request):
    user = request.user
    ordered_cust=None
    customers =  Customer.objects.all()
    for cust in customers:
        if user.username == cust.contact:
            ordered_cust = cust
    if ordered_cust!=None:
        orders = OrderHistory.objects.filter(user_id__exact = ordered_cust.user_id)
    
    return render(request, 'order_history_user.html',{'orders':orders, 'user' : user})


@login_required
def cancel_order(request,pk):
    order = CurrentOrders.objects.get(order_id__exact = pk)
    user = request.user
    ordered_cust=None
    customers =  Customer.objects.all()
    message=[]
    for cust in customers:
        if user.username == cust.contact:
            ordered_cust = cust
    if ordered_cust!=None:
        orders1 = CurrentOrders.objects.filter(user_id__exact = ordered_cust.user_id)
        orders=[]
        ordersNot = CurrentOrders.objects.filter(user_id__exact = ordered_cust.user_id,status="Added to cart")
        for item in orders1 :
            if item not in ordersNot :
                orders.append(item)
    if order.status != "Added to cart" and order.status != "Confirmed":
        message.append("Cannot cancel order as restaurant has begun process!")
        return render(request, 'view_orders.html',{'orders':orders, 'user' : user,'message' : message})

    else:

        CurrentOrders.objects.filter(order_id__exact=pk).update(status = "Cancelled")
        order=CurrentOrders.objects.get(order_id__exact=pk)
        C=OrderHistory(food=order.food,quantity=order.quantity,order_id=order.order_id,user=order.user,rest=order.rest,status=order.status,order_timestamp=order.order_timestamp,amount=order.amount,rating=0.0)
        C.save()
        orders.remove(order)
        order.delete()
        message.append("Order Cancelled !")
        return render(request, 'view_orders.html',{'orders':orders, 'user' : user , 'message' : message})


@login_required
def order_history(request):
    usr=request.user
    crt=[]
    total = 0
    orders = OrderHistory.objects.all()
    for item in orders :
        rest = Restaurant.objects.get(pk=item.rest.rest_id)
        if rest.contact == usr.username and item.status == "Delivered":
            fitem=FoodItems.objects.get(pk=item.food.food_id)
            cust=item.user.name
            total=total+item.quantity*item.amount
            crt.append([fitem.name,cust,item.status,item.quantity,item.amount])
    if len(crt)==0:
        return HttpResponseRedirect("/home/")
    ordered_cust=None
    customers =  Customer.objects.all()
    for cust in customers:
        if usr.username == cust.contact:
            ordered_cust = cust

    return render(request, 'order_history.html', {'cart' : crt, 'total' : total})

@login_required
def inc_count(request,pk):
    q = CurrentOrders.objects.get(order_id__exact = pk).quantity
    CurrentOrders.objects.filter(order_id__exact = pk).update(quantity = q+1)
    return HttpResponseRedirect("/home/")

@login_required
def dec_count(request,pk):
    q = CurrentOrders.objects.get(order_id__exact = pk).quantity
    if q==0:
        #messages.info(request,"Invalid attempt!")
        return HttpResponseRedirect("/home/")
    else:
        CurrentOrders.objects.filter(order_id__exact = pk).update(quantity = q-1)
        if q==1:
            CurrentOrders.objects.filter(order_id__exact = pk).delete()
        return HttpResponseRedirect("/home/")
