from dataclasses import fields
from itertools import chain
from pyexpat import model
from statistics import mode
from unicodedata import category
from aiohttp import request
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from blogapp.models import BlogPost, Category, SubCategory, Message
from django.core.paginator import Paginator

class HomeView(ListView):
    model=BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category)
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug = "yazilim")
        queryset = { 'most_viewed': BlogPost.objects.order_by("-views").filter()[:8] }
        return queryset
    

class CategorySoftwareView(ListView):
    model = BlogPost
    template_name = 'views/category_software.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        category_software = get_object_or_404(Category, slug = "yazilim")
        queryset = BlogPost.objects.filter(category = category_software)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_software = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category_software)
        return context

class CategoryTechnologyView(ListView):
    model = BlogPost
    template_name = 'views/category_technology.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        category = get_object_or_404(Category, slug = "teknoloji")
        queryset = BlogPost.objects.filter(category = category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #category = get_object_or_404(Category, slug = "teknoloji")
        #context['posts'] = BlogPost.objects.filter(category = category)

        category_software = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category_software)
        return context
    
  
class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'views/post_detail.html'

    def updateViews(self):
        post = get_object_or_404(BlogPost, id=self.get_object().id)
        post.views += 1
        post.save()

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        categoryPost = self.get_object().sub_category.id    
        context['categoryPosts'] = BlogPost.objects.order_by("-views").filter(sub_category= categoryPost)[:4]

        category_software = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category_software)

        PostDetailView.updateViews(self)
        return context


    
    





class SoftwareLanguageView(ListView):

    model = BlogPost
    template_name = 'views/software_language.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        language_name = self.kwargs["slug"]
        language = get_object_or_404(SubCategory, slug = language_name)
        queryset = BlogPost.objects.filter(sub_category = language)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language_name = self.kwargs["slug"]
        language = get_object_or_404(SubCategory, slug = language_name)

        category_software = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category_software)
        
        return context

    
    




class ContactView(ListView):
    model = BlogPost
    template_name = 'views/contact.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_software = get_object_or_404(Category, slug = "yazilim")
        context['categories'] = SubCategory.objects.filter(category = category_software)
        return context

    def sendMessage(request):
        if request.method == "GET":
            return redirect("/iletisim") 
        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            newMessage = Message(name = name, email = email, message = message)

            newMessage.save()
            return HttpResponseRedirect("iletisim?success")
