from django.contrib import admin

# Register your models here.


from .models import joueur
from .models import equipe
from .models import ticket

admin.site.register(joueur)
admin.site.register(equipe)
admin.site.register(ticket)
