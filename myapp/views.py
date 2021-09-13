from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context ={
        'name': 'Pat',
        'age': 25,
        'country': 'indo'
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.GET['text']
    words_amount = len(text.split())
    return render(request, 'counter.html', {'amount': words_amount})