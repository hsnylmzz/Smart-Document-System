from django.shortcuts import render

from SDS.myFuncitons import generate_sha
from documents.froms import FileUploadForm
from documents.models import Documents, MyCodes


def home(request):
    template_name = "documents/home.html"
    qm = Documents.objects.all()
    context= { 'qm': qm }
    return render(request, template_name,context=context)

def file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            xfile = Documents (
                # payee=request.user,
                file=request.FILES['File'],
                file_sha1=generate_sha(request.FILES['File'],),
                label=form.cleaned_data.get('Label'),
                # type = form.cleaned_data.get('Type'),
                )
            xfile.save()

            return render(request, 'documents/home.html', {'form' : form})
    else:
        form = FileUploadForm()
    context = {'form': form,}
    return render(request, 'documents/image_form.html', context)

