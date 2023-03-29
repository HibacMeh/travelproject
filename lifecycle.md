#from static files onward 

1) add static files 
2) configure the file's path in django settings use : https://docs.djangoproject.com/en/4.1/howto/static-files/
3) fo to project url aND ADD :

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    
    urlpatterns += static(settings.MEDIA_URL
                          document_root=settings.Media_ROOT)

#django parse thru project url and knows to check setting and realizes the both media and static are saved inside 

4) go to index html and load static    


#models creation 
1) go to models on travelapp 
@) create a class and add models variable 
3. start xamp and add the databse 
4. go to settings and add on db class 
5. make migration and migrate 
6. the values should be visibe

# start admin panel 
1) go to admin page and import the models class and register it 
2) createsuperuser
3)runserver and log into admin portal
4)create fields based on your table 
add def __str__if to rename on models 

5) HTML Parsing using ORM -- go to views and add obj
 obj = Places.objects.all
    return render(request, "index.html", {'result': obj})

6) call the obj on required places 


#django rgistaertion part1
1)make anew app for credentials and add in the settings 
2) add it in the projects  and reidrect to add url
3)app url -specify the view 
4)add fuction in the view and redirect it to templates
5) build a registration form with method post in the credetnials html also add csrf token

6) go to the views page of the app and add the if conditionals for post aand add user.save()
7)log in and it will appaear on postresql 

#check if password are euqal 
8) add an if conditional for password and c passowrd and add else tag on viewpage




