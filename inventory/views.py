from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, AddRecordForm, AddClientForm
from .models import Record, Client


# Create your views here.


def Home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in successfully ")
            return redirect("home")
        else:
            messages.error(request, "something went wrong try again later")
            return redirect("home")
    else:
        return render(request, "inventory/home.html", {"records":records})
    


def logout_user(request):
     logout(request)
     messages.success(request, "you have been logged out ")
     return redirect("home")

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'inventory/register.html', {'form':form})

	return render(request, 'inventory/register.html', {'form':form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'inventory/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'inventory/add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')



def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'inventory/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def add_client(request):
	form = AddClientForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_client = form.save()
				messages.success(request, "Client  Added successfully ...")
				return redirect('show_client')
		return render(request, 'inventory/add_client.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('add_client')


def show_client(request):
	if request.user.is_authenticated:
		# Look Up Records
		client_records = Client.objects.all()
		return render(request, 'inventory/show_client.html', {'client_records':client_records})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	

def CalculateView(request):
	if request.user.is_authenticated:
		records = Record.objects.all()
		total_buying_price = sum(record.buying_price for record in records)
		total_selling_price = sum(record.selling_price for record in records)
		profit = total_selling_price - total_buying_price
		return render(request, "inventory/calculate.html", {
			"total_buying_price": total_buying_price,
			"total_selling_price": total_selling_price,
			"profit": profit,
		})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


		
	

def detail_record(request, pk):
	if request.user.is_authenticated:
		client_record = Client.objects.get(id=pk)
		return render(request, "inventory/client.html", {"client_record": client_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def update_client(request, pk):
	if request.user.is_authenticated:
		current_record = Client.objects.get(id=pk)
		form = AddClientForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('show_client')
		return render(request, 'inventory/update_client.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def delete_client(request, pk):
	if request.user.is_authenticated:
		delete_it = Client.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('show_client')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

     


		



