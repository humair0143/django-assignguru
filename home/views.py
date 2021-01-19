from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")

def contact(request):
    return render(request, "home/contact-us.html")
    
def subjects(request):
    return render(request, "home/subjects.html")

def reviews(request):
    return render(request, "home/reviews.html")

def process(request):
    return render(request, "home/process.html")

def services(request):
    return render(request, "home/services.html")

def samples(request):
    return render(request, "home/samples.html")