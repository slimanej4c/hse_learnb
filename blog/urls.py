from django.urls import path
from .views import SignupView ,LoginView ,LogoutView ,FormationsView, GroupesView ,TokenLoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import get_messages
app_name='blog'
urlpatterns = [
  
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view()),
    path('formations', FormationsView.as_view(), name='formations'),
    path('groupes', GroupesView.as_view(), name='groupes'),
    path('messages', get_messages, name='get_messages'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
  
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

