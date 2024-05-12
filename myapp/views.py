from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse("index page")


def hello(request, username: str):
    return HttpResponse(f"<h1>hello {username}<h1>")


def about(request):
    return HttpResponse("about")


def projects(request):
    projects = list(Proyect.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, title: str):
    query = Task.objects
    task = query.get(title=title)
    return HttpResponse(f"task: {task.title}")
