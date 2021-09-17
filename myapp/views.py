from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'featureloop': features})

def counter(request):
    text = request.POST['text']
    words_amount = len(text.split())
    return render(request, 'counter.html', {'amount': words_amount})