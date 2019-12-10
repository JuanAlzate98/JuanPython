from django.contrib import admin
#importar cada una d elas clases
from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoLogr

admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoLogr)

