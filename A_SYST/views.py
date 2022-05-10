from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import csv
import pandas as pd 
#from A_SYST import main
#from A_SYST import train

def init(request):
    return render(request, "landingpage.html") 

def uploadvideo(request):
    for f in request.FILES.getlist('video'):
        if request.method == 'POST' and f:
            uploaded_file = f
            print(uploaded_file)
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            #extractFrames('./media/'+ uploaded_file.name, './outputdir')
    return render(request, "uploadvideo.html")

def instructor(request):
    csv_fp = open(f'/Users/umairayaz/Downloads/Human_Tagging_And_Tracking/HTAT/A_SYST/attendance.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    #data = pd.read_csv(csv_fp)
   # data_html = data.to_html()
   # context = {'loaded_data': data_html}

    if request.method == 'POST':
        dt= request.POST["dt"]
        with open(f'/Users/umairayaz/Downloads/Human_Tagging_And_Tracking/HTAT/A_SYST/scheduledtime.txt', 'a') as file:
         file.write(dt + "\n")
        request.session['value'] = dt
        print(request.session['value'])
    return render(request, 'instructor.html', {'data' : out, 'headers' : headers})