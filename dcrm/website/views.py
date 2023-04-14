from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login 
from django.contrib import messages
from .forms import SignUpForm
from .models import UserModel
from .forms import AddRecordForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    user_model = UserModel.objects.all()
    
    # check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, ("Welcome ", user.username, " You have been Logged In!"))
            return redirect("home")
        else:
            messages.success(request, "There was an error in login")
            return redirect("home")
    else:
        return render(request, "website/home.html", {"user_model": user_model})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged Out")
    return redirect("home")



def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            
            user_email = form.cleaned_data["email"]
            subject = "Conformation"
            message = f"Dear {username} welcome to tis site"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email]
            
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            
            messages.success(request, "You have been registered")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "website/register.html", {"form": form})

    return render(request, "website/register.html", {"form": form})



def user_record(request, pk):
    if request.user.is_authenticated:
        user_record = UserModel.objects.get(id=pk)
        return render(request, "website/user_record.html", {"user_record": user_record})
    else:
        messages.success(request, "You may not be logged in")
        return redirect("home")
    

def delete_user_record(request, pk):
    if request.user.is_authenticated:
        delete_record = UserModel.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record has been deleted")
        return redirect("home")
    else:
        messages.success(request, "Log in to delete the Record")
        return redirect("home")



def add_user_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_user_record = form.save()
				messages.success(request, "Record hes been Added")
				return redirect('home')
		return render(request, 'website/add_record.html', {'form':form})
	else:
		messages.success(request, "You may not be logged in")
		return redirect('home')



def update_user_record(request, pk):
	if request.user.is_authenticated:
		current_record = UserModel.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been Updated!")
			return redirect('home')
		return render(request, 'website/update_record.html', {'form':form})
	else:
		messages.success(request, "You may not be logged in")
		return redirect('home')

