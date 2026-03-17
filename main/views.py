from django.shortcuts import render
from django.http import HttpRequest
from main.models import Subject, Word

def index_view(request: HttpRequest):

    user = request.user
    subjects = Subject.objects.filter(is_public=True)

    if user.is_authenticated:
        if Subject.objects.filter(author=user).count() > 1:
            subjects = Subject.objects.filter(author=user)
    

    context = {
        "subjects": subjects
    }

    
    return render(request, "index.html", context)

def subject_detail(request: HttpRequest, pk):
    subject = Subject.objects.get(id=pk)

    words = Word.objects.filter(subject=subject)

    context = {
        "subject": subject,
        "words": words
    }
    return render(request, "subject-detail.html", context)