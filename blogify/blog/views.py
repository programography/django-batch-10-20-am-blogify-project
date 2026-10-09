from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import contactus
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

# def privacy_policy(request):
#     return render(request, "about.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

@login_required(login_url = "/login")
def contactuss(request):
    return render(request, "contact.html")

def aboutus(request):
    data = contactus.objects.all().order_by("-id")
    return render(request, "about.html", {"mydata" : data})

def services(request):
    return render(request, "services.html")

def success_message(request):
    return render(request, "saved_page.html")

def contactdatasace(request):
    
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        email = request.POST.get("em")
        p_number = request.POST.get("ph")
        date = request.POST.get("dob")
        gender = request.POST.get("gender")
        messg = request.POST.get("msg")
        imgg = request.FILES.get("img")
                
        data = contactus.objects.create(
            first_name = first_name, last_name = last_name,
            email = email, phone_number = p_number, 
            dob = date, gender = gender, 
            message = messg, q_image = imgg
        )
        
        messages.success(request, "Your information has been saved sucessfully in database...!")
        
        return redirect("sucess_page")
    
    
# CRUD 


def deletecard(request, x):

    data = contactus.objects.get(id = x)
    
    data.delete()
    
    messages.info(request, "data sucessfully deleteed fform database..!")
    
    return redirect("about")


def contact_for_update(request, xyz):
    data = contactus.objects.get(id = xyz)
    return render(request, "contact_for_update.html", {"data" : data, "mynmae" : "Naresh", "Age" : 25})


def updatecntect(request, myid):
    data = contactus.objects.get(id = myid)
    
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        email = request.POST.get("em")
        p_number = request.POST.get("ph")
        date = request.POST.get("dob")
        gender = request.POST.get("gender")
        messg = request.POST.get("msg")
        
        data.first_name = first_name
        data.last_name = last_name
        data.email = email
        data.phone_number = p_number
        data.dob = date
        data.gender = gender
        data.message = messg
        
        data.save()
        
        messages.success(request, "Data updated sucessfully from dataase...!")
    
    return redirect("about")


def signuphere(request):
    if request.method == "POST":
        u_name = request.POST.get("uname")
        email = request.POST.get("email")
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        password = request.POST.get("pass")
        c_pass = request.POST.get("cp")
        
        if password != c_pass:
            messages.warning(request, "Password are't match plese check.")
            return redirect("signup")
        
        if User.objects.filter(username = u_name).exists():
            messages.warning(request, "User with this username already exists please use another one..")
            return redirect("signup")
        
        
        User.objects.create_user(
            username = u_name, first_name = f_name, last_name = l_name,
            email = email, password = password
        )
        
        messages.info(request, "Registration sucessfully done! please login here..")
        
        return redirect("login")
    return render(request, "auth/signup.html")


def loginhere(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pas = request.POST.get("pass")
        
        check = authenticate(username = uname, password = pas)
        
        if check is not None:
            login(request, check)
            messages.success(request, "login sucessfuly done...")
            return redirect("home")
            
        else:
            messages.warning(request, "User not found! please enter valid credicational.!")
            return redirect("login")
    
    return render(request, "auth/login.html")


def logouthere(request):
    logout(request)
    messages.warning(request, "logout done! please login to use this website nicely..")
    return redirect("login")