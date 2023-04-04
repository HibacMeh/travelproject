from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def cred (request):
    #the auth table has been already craeted by django 
    
    if request.method == 'POST':
      username = request.POST['username']
      firstname = request.POST['firstname']
      lastname= request.POST['lastname']
      email = request.POST['email']
      password = request.POST['password']
      cpassword= request.POST['confirm_password']
      
      if password==cpassword:
         #all of these if else cases only happen if the password is correct
         if User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect('cred')
         elif User.objects.filter(email=email).exists():
            messages.info(request, "email is taken")
            return redirect('cred')
         else:
            user = User.objects.create_user(username= username, first_name= firstname, last_name=lastname,email=email,password=password)
            user.save();
         print("user has been saved")

      else:
         messages.info(request, "password not matching")
         return redirect(request, "cred")
      return redirect('/')

      
    return render(request, "cred.html")
