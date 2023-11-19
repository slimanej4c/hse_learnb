from django.db import models


class Forma(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nom) 
class Formation_all(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.PositiveIntegerField()
    def __str__(self):
        return str(self.nom) 
class Groupe_all(models.Model):
    formation = models.ForeignKey(Formation_all, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nombre_de_places = models.PositiveIntegerField()
    duree = models.PositiveIntegerField()
    def __str__(self):
        return str(self.nom) 



"""class UserManager(BaseUserManager):
 

    use_in_migrations = True

    def create_user(self, name, email, password=None):


        if not email:
            raise ValueError('Users must have an email address')

        if not name:
            raise ValueError('Users must have names')

        email = self.normalize_email(email)
        name = name.strip()
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.URLField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email"""
