# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.http import HttpResponse 

from ahren.models import Sheet
from ahren.forms import AddSheetForm
from django.views import generic
from ahren.forms import DeleteSheetForm 


    
def gallery(request):
    query_results = Sheet.objects.all().filter(deleted=1)
    query_results2 = Sheet.objects.all().filter(deleted=0)
    return render(request, 'gallery.html', context={'query_results': query_results,'query_results2': query_results2})

def delete(request):
    query_results = Sheet.objects.all().filter(deleted=1)
    return render(request, 'Delete.html', context={'query_results': query_results})


def home(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'Add.html')
    
    
def addPost(request):
    if request.method == 'POST':
        form = AddSheetForm(request.POST, request.FILES)
        new = Sheet()
        new.name = request.POST['name']
        new.author = request.POST['author']
        new.url = request.FILES['url']
        new.save()
        return HttpResponseRedirect('/Add/')
    else:
        form = AddSheetForm()
        return render(request, 'Add.html', {
            'form': form
        })
    
def deletePost(request):
    if request.method == 'POST':
        form = DeleteSheetForm(request.POST)
        dele = Sheet()
        dele.name = request.POST['name']
        old = dele.search(dele.name)
        old.deleted = 0
        old.save()
        
        
        return HttpResponseRedirect('/Delete/')
    else:
        form = DeleteSheetForm()
        return render(request, 'Delete.html', {
            'form': form
        })
    
class Sheet_ListView(generic.ListView):
    model = Sheet 
    template_name = 'ahren/gallery.html'
    context_object_name = 'Sheet_List'
    
    def get_queryset(self):
        return Sheet.objects()