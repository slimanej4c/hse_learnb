
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# Create your views here.

from django.contrib.auth import authenticate, login
from .models import Formation_all, Groupe_all
from django.conf import settings
    # ...

class TokenLoginView(APIView):
    def post(self, request):
        data = self.request.data
        username = data.get('username')
        password = data.get('password')

        # Authentifiez l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Connexion réussie
            login(request, user)

            # Créez ou récupérez le token d'authentification pour l'utilisateur
            token, created = Token.objects.get_or_create(user=user)

            # Renvoyez le token dans la réponse
            return Response({'token': token.key, 'success': 'User authenticated'})
        else:
            # Échec de l'authentification
            return Response({'error': 'Invalid username or password'})

class FormationsView(APIView):
  
    
    authentication_classes = (TokenAuthentication, )
    permission_classes = ()

    print('user etat')
    
    def get(self, request):
       
        print('user etat:',str(request.user))
        print('user etat:',request.user.is_authenticated)
        print('user etat:',request.user.is_authenticated)
        formations = Formation_all.objects.all()
        data = [{'id': formation.id, 'nom': formation.nom} for formation in formations]
        return Response(data)



class GroupesView(APIView):
   
    authentication_classes = (TokenAuthentication, )
    permission_classes = ()
 

    def get(self, request):
       
        groupes = Groupe_all.objects.all()
        print('user etat:GROUPESSS',request.user.is_authenticated)
        data = [{'id': groupe.id, 'nom': groupe.nom , 'formation':groupe.formation.id,
        'date_debut':groupe.date_debut,'date_fin':groupe.date_fin,
        'nombre_de_places':groupe.nombre_de_places,
        'duree':groupe.duree} for groupe in groupes]
        print(data)
        return Response(data)
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
   
    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        print('in django',username)
        
        try:
            user = auth.authenticate(request,username=username, password=password)
              
            if user is not None:
               
                login(request, user)
                user.backend = settings.AUTHENTICATION_BACKENDS[0]
                #token, created = Token.objects.get_or_create(user=user)
                print('authenticate',request.user)
                
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )
   
    def post(self, request, format=None):
        data = self.request.data
       
        username = data['username']
        password = data['password']
        re_password  = data['re_password']

        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({ 'error': 'Username already exists' })
                else:
                    if len(password) < 6:
                        return Response({ 'error': 'Password must be at least 6 characters' })
                    else:
                        user = User.objects.create_user(username=username, password=password)

                        user = User.objects.get(id=user.id)
                        user.save()

                        return Response({ 'success': 'User created successfully' })
            else:
                return Response({ 'error': 'Passwords do not match' })
        except:
                return Response({ 'error': 'Something went wrong when registering account' })


class LogoutView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        print('logout django ...',request.user.is_authenticated)
        try:
            auth.logout(request)
            print('logout django ...',request.user)
            return Response({ 'success': 'Loggout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })

"""
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get(user_id=serializer.data.get('id'))
            return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAuthUserView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response(data={'error':'No Token. Authorization Denied'}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=request.user.id)
        data = UserSerializer(user).data
        return Response(data)
        
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email == "" or password == "":
            return Response({'error': 'Please provide both email and password'},status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)"""