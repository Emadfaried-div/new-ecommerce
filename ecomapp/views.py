from django.shortcuts import render


# Create your views here.
def home(request):
    name = "Emad" 
    job = "Mechanical engineer"
   
    return render(request, "home.html",{"name":name, "job":job})