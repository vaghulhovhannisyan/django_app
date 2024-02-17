from django.shortcuts import render
from .models import menu

'''def index(request):
    model = menu.objects.all()
    return render(request, 'index.html', {'menu': model})
from django.shortcuts import render
'''

def index(request):
    return render(request, 'index.html')
def django(request):
    return render(request, 'django.html')
def tz(request):
    return render(request, 'ТЗ.html')