# import re
# from django.http import HttpResponse
from django.shortcuts import render
import joblib
from datetime import date

# from sqlalchemy import null

def home(request):
    return render(request,"home.html")

def answer(request,ans):
    return render(request,"answer.html",{"ans":ans})

def result(request):


    if request.method == 'POST':
       
       input_data = request.POST['inputbox']
       
       return answer(request,input_data)

    return render(request,"form.html")
