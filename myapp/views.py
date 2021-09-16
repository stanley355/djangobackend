from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is good'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Bum'
    feature2.is_true = False
    feature2.details = 'Our service is bad'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Bommmmmm'
    feature3.is_true = True
    feature3.details = 'Our service is worst'

    features = [feature1, feature2, feature3]
    
    for feature in features:
        pass

    return render(request, 'index.html', {'featureloop': features})

def counter(request):
    text = request.POST['text']
    words_amount = len(text.split())
    return render(request, 'counter.html', {'amount': words_amount})