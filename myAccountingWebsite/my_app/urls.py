from django.urls import path
from my_app import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about, name='about'),
    path('services',views.services, name='services'),
    path('success',views.success, name='success'),
    path('contact_us', views.contact_us, name='contact_us'),
    
]
