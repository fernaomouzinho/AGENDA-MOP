import calendar
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from django.db.models import Q
from django_summernote.widgets import SummernoteWidget
from agendaapps.event.models import Agenda
from django.forms import DateInput


MONTHS = tuple(zip(range(1,13), (calendar.month_name[i] for i in range(1,13))))
YEARS = tuple(zip(range(2010,2022), range(2010,2022)))


class CalendarPickerForm(forms.Form):
     month = forms.ChoiceField(choices=MONTHS)
     year = forms.ChoiceField(choices=YEARS)

    
class AgendaSearchForm(forms.Form):
    start_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'})
    )
    end_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'})
    )
    
# class AgendaSearchForm(forms.ModelForm):
#     start_date = forms.DateField(label="Data Hahu", widget=DateInput(), required=True)
#     end_date = forms.DateField(label="Data Remata", widget=DateInput(), required=True)
#     class Meta:
#         model = Agenda
#         fields = ['start_date','end_date']
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
           
#             Row(
#                 Column('start_date', css_class='form-group col-md-6 mb-0'),
#                 #Column('end_date', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
           
#             HTML(""" <button class="btn btn-primary" type="submit" title="Rai">Rai <i class="fa fa-save"></i></button> """)
#         )
