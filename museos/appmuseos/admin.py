from django.contrib import admin

from .models import Museum
from .models import Coment
from .models import User
from .models import Configuracion_user
from .models import Page_user


admin.site.register(Museum)
admin.site.register(Coment)
admin.site.register(Configuracion_user)
admin.site.register(Page_user)


