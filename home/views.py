from django.shortcuts import render, get_object_or_404

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Subject, Set, Question

from django.core.mail import send_mail

from django.conf import settings
from django.core.mail import EmailMessage



def home(request):
    return render(request, "home/home.html")

def send_email(subject, body, email):
    try:
        email_msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], reply_to=[email])
        email_msg.send()
        return "Message sent :)"
    except:
        return "Message failed, try again later :("

def contact(request):
    if request.method == "POST":
        send_email(
            request.POST['contact-name'] + " / " + request.POST['contact-subject'] + " / " + request.POST['contact-phone'], 
            request.POST['contact-message'], 
            request.POST['contact-email']
            )
        return render(request, "home/contact-us.html", {'contact_name': request.POST['contact-name']})
    else:
        return render(request, "home/contact-us.html", {})

def reviews(request):
    return render(request, "home/reviews.html")

def process(request):
    return render(request, "home/process.html")

def services(request):

    data = []

    context = {
        'subjects': data,
    }
    return render(request, "home/services.html", context)

def samples(request):
    return render(request, "home/samples.html")

# To list the questions within the selected subject and set
def questions(request, entry, set):
    question = Question.objects.filter(setName_id=set)
    setname = Set.objects.filter(id=set)
    context = {
        'entry': question,
        'entry2': setname,
    }
    return render(request, "home/questions.html", context)

# To list the sets within the subject
def sets(request, entry):
    set = Set.objects.filter(subjectName_id=entry)
    context = {
        'entry': set,
    }
    return render(request, "home/sets.html", context)

# To list the name of subjects
def mcqs(request):

    subject = Subject.objects.all()
    
    context = {
        'subject': subject,
    }

    return render(request, "home/subjects.html", context)


def search(request):

    query = request.GET['query']
    allSets = Set.objects.filter(name__icontains=query)
    

    context = {
        'allSets': allSets,
    }
    return render(request, "home/search.html", context)

def sitemap(request):
    return render(request, "home/sitemap.xml")

