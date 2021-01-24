from django.shortcuts import render

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Set

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