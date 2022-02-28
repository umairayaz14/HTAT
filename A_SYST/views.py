from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def init(request):
    return render(request, "landingpage.html") 

def uploadvideo(request):
    if request.method == "POST":
        uploaded_file = request.FILES["video"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, "uploadvideo.html")

