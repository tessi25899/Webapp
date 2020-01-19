from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from .forms import NewsForm, TopicForm

def index(request):
    context = {'newsletters':News.objects.all(), 'topics': Topic.objects.all()}
    return render(request, template_name="newsletters/news_index.html", context=context)

#news:
def news_show(request, topic):
    if topic == 'Alle':
        context = {'newsletters':News.objects.filter().order_by('published'), 'topics':Topic.objects.all(),}
    else:
        topicid = Topic.objects.get(name=topic)
        print(topicid)
        context = {'newsletters':News.objects.filter(topic=topicid).order_by('published'), 'topics':Topic.objects.all(),}
    return render(request, template_name="newsletters/news_index.html",context=context)
def news_create(request):
    context = {'newsletters':News.objects.all(), 'topics': Topic.objects.all(),'message':'Nachricht erstellen'}
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect(reverse('newsletters:news_index'))
    else:
        form = NewsForm()
    context = {'newsletters':News.objects.all(), 'topics': Topic.objects.all(),'form':form,'message':'Nachricht erstellen'}
    return render(request, 'newsletters/news_form.html', context=context )
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {'news':News.objects.all().order_by('published'),'topics':Topic.objects.all()}
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            print(news.published)
            news = form.save(commit=False)
            news.save()
            return redirect(reverse('newsletters:news_index'))
        else:
            print("not valid")
    else:
        form = NewsForm(instance=news)
    context = {'news':News.objects.all().order_by('published'),'topics':Topic.objects.all(),'form':form, 'titel':'Nachricht bearbeiten'}
    return render(request, 'newsletters/news_form.html', context=context )
def news_delete(request,pk):
    try:
        News.objects.get(pk=pk).delete()
    finally:
        return redirect(reverse('newsletters:news_index'))

#topic
def topic_show(request):
    context = {'topics':Topic.objects.all()}
    return render(request, template_name="newsletters/topic_index.html",context=context)
def topic_create(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.save()
            print("create")
            return redirect(reverse('newsletters:topic_show'))
    else:
        form = TopicForm()
    context = {'topics':Topic.objects.all(),'form':form, 'titel':'Thema bearbeiten'}
    return render(request, 'newsletters/topic_form.html', context=context )
def topic_edit(request, pk):
    news = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = TopicForm(request.POST, instance=news)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.save()
            return redirect(reverse('newsletters:topic_show'))
        else:
            print("not valid")
    else:
        form = TopicForm(instance=news)
    context = {'topics':Topic.objects.all(), 'form':form, 'titel':'Kategorie bearbeiten'}
    return render(request, 'newsletters/topic_form.html', context=context )
def topic_delete(request,pk):
    try:
        Topic.objects.get(pk=pk).delete()
    
    finally:
        return redirect(reverse('newsletters:topic_show'))

