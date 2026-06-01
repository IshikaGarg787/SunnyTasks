from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    if request.method == "POST":

        title = request.POST.get("task_title")

        if title:
            Task.objects.create(
    user=request.user,
    title=title
)

        return redirect("home")

    tasks = Task.objects.filter(
    user=request.user
)

    context = {
        "tasks": tasks
    }

    return render(
        request,
        "tasks/home.html",
        context
    )

def delete_task(request, task_id):

    task = Task.objects.get(
    id=task_id,
    user=request.user
)
    task.delete()

    return redirect("home")

def complete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.completed = True

    task.save()

    return redirect("home")