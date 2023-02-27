from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views




urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
