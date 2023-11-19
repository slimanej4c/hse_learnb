from django.contrib import admin

# Register your models here. admin admin

from .models import Formation_all ,Groupe_all ,Forma
# Register your models here.
admin.site.register(Formation_all)
admin.site.register(Groupe_all)
admin.site.register(Forma)