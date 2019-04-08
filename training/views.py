from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h2>Hey there</h2>')
    return render(request, "training/temp/TEST.HTML")

def search(request):
    return HttpResponse('<h2>Search Page</h2>')