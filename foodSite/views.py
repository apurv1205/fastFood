from foodSite.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from foodSite.models import *
import editdistance

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            stat = form.cleaned_data['choice_field']
            status="C";
            print stat,"1"
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
            return HttpResponseRedirect('success/')
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
 
@login_required
def home(request):

    menu = FoodItems.objects.all()
    restaurants = Restaurant.objects.all()
    cart = CurrentOrders.objects.all()
    usr=request.user
    crt=[]
    total=0
    for item in cart :
        customer = Customer.objects.get(pk=item.user.user_id)
        if customer.contact == usr.username and item.status == "Added to cart":
            fitem=FoodItems.objects.get(pk=item.food.food_id)
            ritem=Restaurant.objects.get(pk=item.rest.rest_id)
            total=total+item.quantity*item.amount
            crt.append([fitem.name,ritem.name,item.amount,item.quantity,item.status])
    
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

def rest_detail(request, pk):
    menu = FoodItems.objects.all()
    items=[]
    for item in menu:
        if str(item.rest) == str(pk) : 
            items.append(item)
    rest = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'rest_detail.html', {'items': items})

def cart(request, pk):
    item = get_object_or_404(FoodItems, pk=pk)
    customers = Customer.objects.all()
    orders=CurrentOrders.objects.all()
    user=request.user
    for cust in customers :
        if user.username == cust.contact :
            flag=False
            for thing in orders :
                if thing.user.user_id==cust.user_id and thing.food.food_id == item.food_id:
                    CurrentOrders.objects.filter(pk=thing.pk).update(quantity=thing.quantity + 1)
                    flag=True
            if flag==False :
                C=CurrentOrders(user=cust,rest=item.rest,status="Added to cart",amount=item.price,food=item,quantity=1)
                C.place_order()
    return render(request, 'cart.html', {'item': item})