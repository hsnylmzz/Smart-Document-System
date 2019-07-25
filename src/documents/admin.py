from django.contrib import admin
from documents.models import Documents, DocumentsOwner, MyCodes

# Register your models here.


admin.site.register(Documents)
admin.site.register(DocumentsOwner)
admin.site.register(MyCodes)

