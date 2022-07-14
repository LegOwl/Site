from turtle import home
from django.contrib import admin
from django.urls import path, re_path
from blog.views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('about/', About.as_view(), name = 'about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name ='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('cats/<slug:cat>', categories),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]


