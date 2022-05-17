from django.shortcuts import render,redirect,HttpResponse
from http import HTTPStatus
from django.contrib.auth import login, authenticate, logout#add this
from django.contrib.auth.forms import AuthenticationForm #add this
import json
from . models import Employee
# from django.contrib.auth import login, authenticate, logout #add this
# Create your views here.

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("demosampleapp:fileupload")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def homepage(request):
    return render(request=request,template_name="homepage.html")



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("demosampleapp:fileupload")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("demosampleapp:login")


def post_article(request):      #sample is the http request   
	if request.method == 'POST':
		sample = request.FILES['myfile']
		json_data = sample.read()
		data = json.loads(json_data)
		students = []
		for each_student in data:
			a = each_student['employee_name']
			employee_departmentname = each_student['employee_department']
			employee_phonenumbername = each_student['employee_phonenumber']
			employee_office_branchname = each_student['employee_office_branch']
			response_data = {}
			response_data['employee_name'] = a
			response_data['employee_department'] = employee_departmentname
			response_data['employee_phonenumber'] = employee_phonenumbername
			response_data['employee_office_branch'] = employee_office_branchname
			employee = Employee()
			employee.employee_name = a
			employee.employee_department = employee_departmentname
			employee.employee_phonenumber = employee_phonenumbername
			employee.employee_office_branch = employee_office_branchname
			employee.save()
			students.append(response_data)
		# return HttpResponse(json.dumps(students), content_type="application/json")
		return render(request = request,template_name='allrecords.html',context={"employees":Employee.objects.all()})
	else:
		return render(request= request,template_name='fileupload.html')



def all_records(request):
	employee = Employee.objects.all()
	return render(request,'allrecords.html',{"employees":employee})
