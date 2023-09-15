from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cruises_index(request):
    cruises = Cruises.objects.all()
    return render(request, 'cruises/index.html', {
        'cruises': cruises
    })
