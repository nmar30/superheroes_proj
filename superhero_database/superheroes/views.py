from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    all_superheroes = Superhero.objects.all()
    context = {'all_superheroes': all_superheroes}
    return render(request, 'superheroes/index.html', context)

def detail(request, superhero_id):
    one_superhero = Superhero.objects.get(pk=superhero_id)
    context = {'one_superhero': one_superhero}
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        catchphrase = request.POST.get('catchphrase')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        new_superhero = Superhero(name=name, catchphrase=catchphrase, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete(request, superhero_id):
    delete_superhero = Superhero.objects.get(pk=superhero_id)
    delete_superhero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))

def edit(request, superhero_id):
    if request.method == 'POST':
        sh = Superhero.objects.get(pk=superhero_id)
        sh.name = request.POST.get('name')
        sh.catchphrase = request.POST.get('catchphrase')
        sh.alter_ego = request.POST.get('alter_ego')
        sh.primary_ability = request.POST.get('primary_ability')
        sh.secondary_ability = request.POST.get('secondary_ability')
        sh.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        edit_superhero = Superhero.objects.get(pk=superhero_id)
        context = {'edit_superhero': edit_superhero}
        return render(request, 'superheroes/edit.html', context)