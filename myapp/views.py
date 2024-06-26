from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject


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
    return render(request, "projects/projects.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()

    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_task(request):
    flag = False
    if request.method == "GET":
        # interface
        return render(
            request, "tasks/create_task.html", {"form": CreateNewTask, "flag": flag}
        )
    elif request.method == "POST":
        Task.objects.create(
            title=request.POST["title"],
            descritption=request.POST["description"],
            project_id=1,
        )
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(
            request, "projects/create_project.html", {"form": CreateNewProject}
        )
    else:
        Proyect.objects.create(name=request.POST["name"])
        return redirect("projects")
