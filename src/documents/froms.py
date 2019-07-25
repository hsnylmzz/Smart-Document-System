from django import forms

from SDS.myFuncitons import generate_sha, Kodlar
from documents.models import Documents, MyCodes


class FileUploadForm(forms.Form):
    Label = forms.CharField(max_length=21, required=True)
    File = forms.FileField(required=True)

    # Type = forms.ModelChoiceField(queryset=MyCodes.objects.all())

    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        Label = cleaned_data.get('Label')
        File = cleaned_data.get('File')
        # Type = cleaned_data.get('Type')
        sha1 = generate_sha(File)
        if Documents.objects.filter(file_sha1=sha1).exists():
            raise forms.ValidationError('Eklemeye çalıştığınız dosya sistemede mevcut')
        if not Label:
            raise forms.ValidationError('Başlık Alanı boş bırakıldı')
        if not File:
            raise forms.ValidationError('Dosya eklemeyi unuttunuz')
