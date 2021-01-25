from django.shortcuts import render, get_object_or_404

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Set

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

def entry(request, entry):
    set1 = Set.objects.filter(setName=entry)
    context = {
        'entry': set1
    }
    return render(request, "home/mcqs.html", context)

def mcqs(request):

    set1 = Set.objects.all()
    arr1 = []
    for a in set1:
        arr1.append(a.setName)
    
    arr1 = list(dict.fromkeys(arr1))
    
    context = {
        'object': arr1
    }

    return render(request, "home/mcqs.html", context)

@permission_required('admin.can_add_log_entry')
def set_upload(request):

    prompt = {
        'order': 'Order of csv should be Set Name, Question, Answers',
    }

    if request.method == "GET":
        return render(request, "home/upload.html", prompt)
    
    # grab the file from the form
    csv_file = request.FILES['file']
    
    #check if it's csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)

    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Set.objects.update_or_create(
            setName = column[0],
            question = column[1],
            answer = column[2],
        )

    context = {}
    return render(request, "home/upload.html", context)
