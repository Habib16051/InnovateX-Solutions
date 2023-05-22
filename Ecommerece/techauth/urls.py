from django.urls import path
from techauth import views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate')


]
