import calendar
from django import forms


MONTHS = tuple(zip(range(1,13), (calendar.month_name[i] for i in range(1,13))))
YEARS = tuple(zip(range(2010,2022), range(2010,2022)))


class CalendarPickerForm(forms.Form):
     month = forms.ChoiceField(choices=MONTHS)
     year = forms.ChoiceField(choices=YEARS)

    
     