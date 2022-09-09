from django.contrib import admin
from django.urls import path
from  app import views
urlpatterns = [
    path('', views.hike ,name='hike'),
    path('run', views.run ,name='run'),
    path('go', views.go ,name='go'),
    path('contact', views.contact ,name='contact'),
    path('about', views.about ,name='about'),
    path('signup', views.signup ,name='signup'),
    path('login', views.login ,name='login'),
    path('admlogin', views.admlogin ,name='admlogin'),
    path('add', views.add ,name='add'),
    path('profile', views.profile ,name='profile'),
    path('complaint', views.complaint ,name='complaint'),
    path('reg', views.reg ,name='reg'),

]
