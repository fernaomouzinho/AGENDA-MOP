from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Agenda, Informative, CommentInformative


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('user', 'title_slug','is_cancel', 'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),
          
        }
        
class PostponedAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('user', 'title_slug','invitedinstitue', 'is_cancel', 'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),
          
        }

class CommentAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('user', 'title','title_slug','invitedinstitue', 'attendence','start_time','end_time','location','is_cancel', 'is_active', 'status')
       

class InformativeForm(forms.ModelForm):
    class Meta:
        model = Informative
        #fields = ('user','title', 'title_slug', 'description','is_done',)
        exclude = ('user','title_slug','is_cancel', 'is_active' )

class CommentInformativeForm(forms.ModelForm):
    class Meta:
        model = CommentInformative
        exclude = ('user', 'informative', 'is_active',)
       