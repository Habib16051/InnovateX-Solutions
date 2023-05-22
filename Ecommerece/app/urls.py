
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name="HandleRequest")




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
