from django.shortcuts import redirect, render
from .models import Countries, Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects, paginateProjects
# Create your views here.

def projects(request):
    projects, search_query= searchProjects(request)
    custom_range, projects = paginateProjects(request,projects,3 )

    context= {
        "projects":projects,
        "search_query":search_query,
        "custom_range":custom_range
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    owner_projects = Project.objects.filter(owner=project.owner.id)
    context= {
        "project": project,
        "owner_projects":owner_projects
    }
    return render(request, 'projects/single_project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile= request.user.profile
    form = ProjectForm()
    if request.method== 'POST':
        form = ProjectForm(request.POST, request.FILES)
        newTags = request.POST.get('newTags').replace(',', " ").split()

        if form.is_valid:
           project= form.save(commit=False)
           project.owner = profile
           project.save()
           for country in newTags:
                country, created = Countries.objects.get_or_create(name=country)
                project.countries.add(country)
           messages.success(request, "Project Added Successfully")
           return redirect('account')
    context ={
        'form': form

    }
    return render(request, 'projects/project_form.html', context)
@login_required(login_url="login")
def updateProject(request, pk):
    profile= request.user.profile
    project= profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    newTags = request.POST.get('newTags')

    if request.method == 'POST' :
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            project=form.save()
            for country in newTags:
                country, created = Countries.objects.get_or_create(name=country)
                project.countries.add(country)
            return redirect('projects')
    context={
        'form': form
    }
    return render(request, 'projects/project_form.html', context)
@login_required(login_url="login")
def deleteProject(request, pk):
    profile= request.user.profile

    obj= profile.project_set.get(id=pk)
    if request.method== 'POST':
         obj.delete()
         messages.success(request, 'Project Deleted successfuly')
         return redirect('account')
    context={
        "obj":obj
    }
    return render(request, 'delete_template.html', context)
