from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('user','title', 'title_slug', 'description','start_time','end_time','is_cancel',)
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),
          
        }