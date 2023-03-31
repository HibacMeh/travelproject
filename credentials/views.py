from collections import UserList, UserString
from site import USER_BASE
from django.shortcuts import render

# Create your views here.
def cred (request):
    if request.method == 'POST':
      firstname = request.POST['firstname']
      lastname= request.POST['lastname']
      email = request.POST['email']
      password = request.POST['password']
      cpassword= request.POST['confirm_password']

      user = UserString.objects.create_user(firstname= firstname, lastname=lastname,email=email,password=password)

      

    return render(request, "cred.html")



