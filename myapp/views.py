from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import render


# Create your views here.
def index(request):
    title = "Welcome to django course"
    return render(
        request,
        "index.html",
        {
            "title": title,
        },
    )


def hello(request, username: str):
    return HttpResponse(f"<h1>hello {username}<h1>")


def about(request):
    return render(request, "about.html")


def projects(request):
    # projects = list(Proyect.objects.values())
    query = Proyect.objects
    projects = query.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})
