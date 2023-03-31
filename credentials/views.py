from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def cred (request):
    #the auth table has been already craeted by django 
    
    if request.method == 'POST':
      firstname = request.POST['firstname']
      lastname= request.POST['lastname']
      email = request.POST['email']
      password = request.POST['password']
      cpassword= request.POST['confirm_password']
      
      if password==cpassword:
         user = User.objects.create_user(firstname= firstname, lastname=lastname,email=email,password=password)
         user.save();
         print("user has been saved")

      else:
         print("password not matching")

      

    return render(request, "cred.html")


