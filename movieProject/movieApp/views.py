
# Create your views here.
from django.shortcuts import render, get_object_or_404

# functions that render the html pages


# Create your views here.
def index(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")