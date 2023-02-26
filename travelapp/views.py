from django.shortcuts import render

# Create your views here

def demo(request) :
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")
def blah(request):
    return render(request, "blah.html")
    
