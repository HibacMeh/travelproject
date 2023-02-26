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

