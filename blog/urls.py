from django.urls import path
from .views import SignupView ,LoginView ,LogoutView ,FormationsView, GroupesView ,TokenLoginView


app_name='blog'
urlpatterns = [
  
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view()),
    path('formations', FormationsView.as_view(), name='formations'),
    path('groupes', GroupesView.as_view(), name='groupes'),
   
   
]