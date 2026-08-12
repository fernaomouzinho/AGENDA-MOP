from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Institution, Attendence


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        exclude = ('id',)

class AttendenceForm(forms.ModelForm):
    class Meta:
        model = Attendence
        exclude = ('id',)

