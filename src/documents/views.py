from django.shortcuts import render
from documents.models import *

# Create your views here.
def index(request):
    template_name="documents/index.html"
    q= Documents.objects.all()
    context = {
        'q':q
    }
    return render(request,template_name,context=context)
