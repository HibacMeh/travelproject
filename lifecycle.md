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

