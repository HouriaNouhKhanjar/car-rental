from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'car/index.html')

# Create your views here.
def detail(request):
    return render(request, 'car/car-detail.html')