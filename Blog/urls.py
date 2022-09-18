from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blogapp.urls")),
    path('post/<int:pk>/', include("blogapp.urls")),
    path('yazilim', include("blogapp.urls")),
    path('teknoloji', include("blogapp.urls")),
    path('iletisim', include("blogapp.urls")),
    path('yazilim/<slug:slug>/', include("blogapp.urls")),


]