from django.contrib import admin
from .models import Imgminer
from .models import Chemform
from .models import Chemical
from .models import Ierchem
from .models import Ierin
from .models import Ierphy
from .models import Interface
from .models import Physic
admin.site.register(Imgminer)
admin.site.register(Chemform)
admin.site.register(Chemical)
admin.site.register(Ierchem)
admin.site.register(Ierin)
admin.site.register(Ierphy)
admin.site.register(Interface)
admin.site.register(Physic)