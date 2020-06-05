from django.shortcuts import render, redirect
from DjangoCRUD.models import Person
from DjangoCRUD.forms import PersonForm


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/DjangoCRUD/list')
            except:
                pass
    else:
        form = PersonForm()
    return render(request, 'DjangoCRUD/index.html', {'form': form})


def list_person(request):
    people = Person.objects.all()
    return render(request, "DjangoCRUD/list.html", {'people': people})


def edit_person(request, firstName):
    person = Person.objects.get(firstName=firstName)
    return render(request, 'DjangoCRUD/edit.html', {'person': person})


def update_person(request, firstName):
    person = Person.objects.get(firstName=firstName)
    form = PersonForm(request.POST, instance=person)
    if form.is_valid():
        form.save()
        return redirect("/DjangoCRUD/list")
    return render(request, 'DjangoCRUD/edit.html', {'person': person})


def delete_person(request, firstName):
    person = Person.objects.get(firstName=firstName)
    person.delete()
    return redirect("/DjangoCRUD/list")
