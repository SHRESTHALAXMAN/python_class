from django.shortcuts import HttpResponse, render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def create(request):
    error = None
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        if not name or not description:
            error = "Both name and description are required."
        else:
            return render(request, "create.html", {'error': error})

        Task.objects.create(
            name=name,
            description=description
        )
        return redirect('/')

    return render(request, "create.html")


def mark(request, pk):
    task = Task.objects.get(id=pk)
    task.status = True
    task.save()
    return redirect('/')
