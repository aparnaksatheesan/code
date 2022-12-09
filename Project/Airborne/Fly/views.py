from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AircraftForm
from .models import Aircraft


# Create your views here.
def creation(request):
    object = Aircraft.objects.all()
    return render(request, 'creation.html', {'result': object})


def detail(request, id):
    aircraft = Aircraft.objects.get(id=id)
    return render(request, 'detail.html', {'aircraft': aircraft})


def add_products(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        image = request.FILES['image']
        aircraft = Aircraft(name=name, image=image, description=description)
        aircraft.save()
    return render(request, 'add.html')


def update(request, id):
    aircraft = Aircraft.objects.get(id=id)
    form = AircraftForm(request.POST or None, request.FILES, instance=aircraft)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'aircraft': aircraft})


def delete(request, id):
    if request.method == 'POST':
        aircraft = Aircraft.objects.get(id=id)
        aircraft.delete()
        return redirect('/')
    return render(request, 'delete.html')
