from unicodedata import name
from django.urls import path
from .views import *
from blogapp import views

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('yazilim', CategorySoftwareView.as_view(), name='category_software'),
    path('teknoloji', CategoryTechnologyView.as_view(), name='category_technology'),
    path('iletisim', ContactView.as_view(), name='contact'),
    path('yazilim/<slug:slug>/', SoftwareLanguageView.as_view(), name='software_language'),
    path('sendmessage', views.ContactView.sendMessage),

   
]
