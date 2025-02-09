from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from.models import Inventory,Category
from.form import InventoryForm
from inventory_system.settings import LOW_QUANTITY

def login_user(request):
    

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfully')
            return redirect('index')
        else:
            messages.success(request,'Wrong username or password combination')
            return redirect('home')
    else:
        return  render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'you have log out............')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'user is arleady exists')
                return redirect('register')
            elif len(password)<8 or len(password1)<8:
                messages.error(request, 'The password should contain 8 charater')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request, 'You have been registered to the system')
                return redirect('login')
        else:
            messages.error(request, 'Two password doesnot match.try again')
            return redirect('register')
    else:


        return render(request, 'register.html')


def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')


def dashboard(request):
    items=Inventory.objects.filter(user=request.user).order_by('id')
    low_invetory=Inventory.objects.filter(
        user=request.user,
        quantity__lte= LOW_QUANTITY
    )
    if low_invetory.count()>0:
        if low_invetory.count()>1:
             messages.success(request,f'{low_invetory.count()} item have low inventory')
        else:
            messages.success(request, f'{low_invetory.count()},Item has low inventory')

    low_invetory_ids=Inventory.objects.filter(
        user=request.user,
        quantity__lte=LOW_QUANTITY
    ).values_list('id',flat=True)

    return render(request,'dashboard.html',{'items':items,'low_invetory_ids':low_invetory_ids})



def add_record(request):
    form=InventoryForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request, 'record added successfully')
                return redirect('dashboard')


        return render(request, 'add.html',{'form':form})
    else:
        messages.success(request, 'record you must login')
        return redirect('login')

def update_inventory(request,pk):
    if request.user.is_authenticated:
        curent=Inventory.objects.get(id=pk)
        form = InventoryForm(request.POST or None,instance=curent)
        if form.is_valid():
            form.save()
            messages.success(request, 'record updated successfully')
            return redirect('dashboard')
        return render(request, 'update.html', {'form': form})
    else:
        messages.error(request, 'You must login to the system')
        return redirect('login')



def delete_record(request,pk):
    if request.user.is_authenticated:
       item =Inventory.objects.get(id=pk)
       if request.method == 'POST':  # Confirm deletion
           item.delete()
           messages.success(request, 'Item deleted successfully.')
           return redirect('dashboard')  # Redirect to inventory list after deletion
    
       return render(request, 'delete.html', {'item': item})
def about(request):
    return render(request,'about.html')


def service(request):
    return render(request,'service.html')


def contact(request):
    return render(request,'contact.html')