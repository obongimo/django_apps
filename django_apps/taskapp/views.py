from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task: ", min_length=1, max_length=100)

def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, "taskapp/index.html", {
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse("taskapp:index"))
    
    else:
        form= NewTaskForm()

    return render(request, "taskapp/add_task.html", {
        "form": form
    })