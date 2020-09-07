from django.shortcuts import render,redirect
from .models.UserModel import Users
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'login.html')


def login(request):
	if request.method == 'POST':
		uname=request.POST['uname']
		password=request.POST['paswd']
		finduser=Users.objects.filter(username=uname)
		if finduser:
			return render(request,'homepage.html')
		else:
			return HttpResponse('User not found')




def register(request):
	if request.method == 'POST':
		fname= request.POST['fname']
		lname= request.POST['lname']
		email= request.POST['email']
		uname= request.POST['uname']
		passwd= request.POST['passwd']
		confpas= request.POST['confpas']
		if passwd == confpas:
			user=Users()
			user.firstname=fname
			user.lastname=lname
			user.username=uname
			user.email=email
			user.password=passwd
			user.save()
			return HttpResponse('Data Saved')
			
	elif request.method == 'GET':
		return render(request,'register.html')
