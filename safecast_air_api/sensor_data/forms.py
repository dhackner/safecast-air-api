from django.forms import ModelForm

from .models import RawReading


class RawReadingForm(ModelForm):

    class Meta:
        model = RawReading
        fields = ['raw_json']
