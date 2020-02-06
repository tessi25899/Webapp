from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from webapp.utils import *
from django.http import Http404  
import os
from django.http import FileResponse
from django.utils.text import slugify
from .forms import FiledocumentForm, CommentaryForm

def index(request):
    documents = Filedocument.objects.all()
    c_admin = check_admin(request.user)
    
    context = {'documents':documents, 'c_admin':c_admin}
    return render(request, template_name="documents/index.html",context=context)

def detail(request, name):
    documents = Filedocument.objects.all()
    docfile = Filedocument.objects.get(name=name)
    c_admin = check_admin(request.user)
    comments = Commentary.objects.filter(filedocument=docfile.id)
    context = {'docfile':docfile,'documents':documents, 'c_admin':c_admin,'comments':comments}
    return render(request, template_name="documents/detail.html",context=context)

def document_create(request):
    documents = Filedocument.objects.all()
    c_admin = check_admin(request.user)

    if request.method == "POST":
        form = FiledocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()
            return redirect(reverse('documents:documents_index'))
    else:
        form = FiledocumentForm()
    context = {'documents':documents, 'c_admin':c_admin,'form':form, 'titel':'Dokument hochladen'}
    return render(request, 'documents/file_form.html', context=context )

def document_edit(request, pk):
    doc = get_object_or_404(Filedocument, pk=pk)
    documents = Filedocument.objects.all()
    c_admin = check_admin(request.user)

    if request.method == "POST":
        form = FiledocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()
            return redirect(reverse('documents:documents_index'))
    else:
        form = FiledocumentForm(instance=doc)
    context = {'documents':documents, 'c_admin':c_admin,'form':form, 'titel':'Dokument hochladen'}
    return render(request, 'documents/file_form.html', context=context )

def delete(request,pk):
    try:
        filedoc = Filedocument.objects.get(pk=pk)
        if filedoc.owner.id == request.user.id or check_admin(request.user) == True:
            filedoc.delete()
    finally:
        return redirect(reverse('documents:documents_index'))

def document_download(request, id):
    item = get_object_or_404(Filedocument, pk=id)
    file_name, file_extension = 	 os.path.splitext(item.document.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.document.file, 
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.name)[:100], file_extension)
    return response