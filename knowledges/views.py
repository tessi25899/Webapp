from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

def index(request):
    context = {'objects':Fwdv.objects.all(), 'titel': "FwDVs"}
    return render(request=request, template_name="knowledges/index.html",context=context)

def index_fwdv(request):
    context = {'objects':Fwdv.objects.all(), 'titel': "FwDVs"}
    return render(request=request, template_name='knowledges/index_fwdv.html',context=context)

def index_knowledge(request, slug):
    context = {'objects':Knowledge.objects.all(),'fwdvID':Fwdv.objects.get(slug=slug) ,'titel': slug}
    return render(request=request, template_name='knowledges/detail.html',context=context)

def index_content(request, slug, id):
    context = {'objects':Knowledge.objects.all(),'fwdvID':Fwdv.objects.get(slug=slug) ,'titel': slug}
    return render(request=request, template_name='knowledges/detail.html',context=context)



class KnowledgeDetailView(generic.DetailView):
    model = Knowledgecontent
    template_name = 'knowledges/detail_content.html'