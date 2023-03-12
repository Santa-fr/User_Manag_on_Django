from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Utilisateur
from .forms import UtilisateurForm


@login_required()
def all_utilisateurs_view(request):
    utilisateurs = Utilisateur.objects.all()
    context = {
        'users':utilisateurs
    }
    return render(request, "utilisateurs/list.html", context)


def create_utilisateur_view(request):
    form = UtilisateurForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UtilisateurForm()
    context = {
        'form': form
    }
    return render(request, "utilisateurs/create_utilisateur.html", context)


def delete_utilisateur_view(request, id):
    obj = get_object_or_404(Utilisateur, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "utilisateurs/delete_utilisateur.html", context)

def update_utilisateur_view(request, id=id):
    obj = get_object_or_404(Utilisateur, id=id)
    form = UtilisateurForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "utilisateurs/create_utilisateur.html", context)                  
            

