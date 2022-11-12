from django.shortcuts import render
from django.http import HttpResponse
from .models import phishing
import pickle
import os
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

from pathlib import Path


def phishing(request):
    return render(request, 'phishing.html')


def prediction(request):
    print(request)
    if request.method == 'POST':
        # print(request.POST.dict())
        temp = {}
        temp['urls'] = request.POST.get('urls')
        print(os.path.join(Path(__file__).resolve().parent, 'model.sav'))
        model = pickle.load(
            open(os.path.join('C:/Users/Roshini/Desktop/new', 'model.sav'), "rb"))
        result = model.predict([temp['urls']])
    context = {'a': result}
    return render(request, 'phishing.html', context)
