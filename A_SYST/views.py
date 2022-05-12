from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import csv
import pandas as pd 
#from A_SYST import main
#from A_SYST import train
import os
from subprocess import call
from subprocess import Popen
import subprocess
import runpy

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
    csv_fp = open(f'./A_SYST/attendance.csv', 'r')
    csv_fp.readline()
    session = csv_fp.readline()
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    #out = [row for row in reader]
    out = []
    for row in reader:
        #if ('Session' in row['Sr_no']):

      if row['Sr_no'] is None:
          row['Sr_no'] = " "

      if row['Name'] is None:
          row['Name'] = " "

      if row['Time'] is None:
          row['Time'] = " "

      out = out + [row]
          #yz = row['Sr_no']
        #else:
          #out = out + [row]
    #data = pd.read_csv(csv_fp)
   # data_html = data.to_html()
   # context = {'loaded_data': data_html}

    if request.method == 'POST':
        dt= request.POST["dt"]
        with open(f'./A_SYST/scheduledtime.txt', 'a') as file:
         file.write(dt + "\n")
        request.session['value'] = dt
        print(dt)
    return render(request, 'instructor.html', {'data' : out, 'headers' : headers, 'xy' : session,})

def trainmodel(request):
    #from A_SYST import fypmodel
    #os.system('python ./A_SYST/fypmodel.py')
    #call(["python", "./A_SYST/fypmodel.py"])
    #Popen(['python3', './A_SYST/fypmodel.py'])
    #runpy.run_path(path_name='./A_SYST/fypmodel.py')
    subprocess.Popen(['python3', "./A_SYST/fypmodel.py"])
    #os.startfile('./A_SYST/fypmodel.py')
    return render(request, "uploadvideo.html") 