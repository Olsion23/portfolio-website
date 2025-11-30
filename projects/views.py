from django.shortcuts import render, redirect, get_object_or_404
from.models import Project, Skill, Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.contrib.staticfiles import finders

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    print("✅ Home view executed")
    return render (request, 'projects/home.html', {'projects':projects, 'skills':skills})
# Create your views here.
@login_required
def project_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        image = request.FILES.get('image')
        Project.objects.create(title=title, descriptions=description, link=link, image=image)
        messages.success(request, 'Project created sucessfully!')
        return redirect('home')
    return render(request, 'projects/project_form.html')

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.title = request.POST['title']
        project.descriptions = request.POST['description']
        link = request.POST.get('link', '')
        if link and not link.startswith (('http://', 'https://')):
            link = 'https://' + link
        project.link = link
        if request.FILES.get('image'):
            project.image = request.FILES['image']
        project.save()
        messages.success(request, 'Project updatet sucessfully!')
        return redirect('home')
    return render(request, 'projects/project_form.html', {'project':project})
    

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
       project.delete()
       messages.warning(request, 'Project deleted sucessfully!')
       return redirect('home')
    
    return render(request, 'projects/project_confirm_delete.html', {'project':project})

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        messages.success(request, 'Your message has been sent sucessfully!')
        return redirect('home')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, 
                            username = request.POST['username'],
                            password = request.POST['password']
                            )
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credencials!')
    return render(request, 'projects/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
        

def download_cv(request):
    cv_path = finders.find('files/Olsion_Bejleri_Professional_CV.pdf')
    
    if os.path.exists(cv_path):
        return FileResponse(open(cv_path, 'rb'), as_attachment=True, filename='Olsion_Bejleri_Professional_CV.pdf')
    else:
        raise Http404('CV not found!')


def view_cv(request):
    cv_path = finders.find('files/Olsion_Bejleri_Professional_CV.pdf')
    if os.path.exists(cv_path):
       
        return FileResponse(open(cv_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404("CV file not found.")