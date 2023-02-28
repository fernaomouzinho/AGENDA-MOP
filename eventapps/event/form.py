from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import CatAgenda, Agenda, RequestAgenda, Informative, CommentInformative


class CategoryAgendaForm(forms.ModelForm):
    class Meta:
        model = CatAgenda
        exclude = ('id',)


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('user', 'title_slug', 'is_cancel',
                   'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),

        }


class PostponedAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('user', 'title_slug', 'invitedinstitue',
                   'is_cancel', 'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),

        }


class CommentAgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        exclude = ('user', 'title', 'title_slug', 'invitedinstitue',
                   'start_time', 'end_time', 'location', 'is_cancel', 'is_active', 'status')


class RequestedAgendaForm(forms.ModelForm):

    class Meta:
        model = RequestAgenda
        exclude = ('user', 'title_slug',
                   'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),

        }


class InformativeForm(forms.ModelForm):
    class Meta:
        model = Informative
        exclude = ('user', 'title_slug', 'observation',
                   'is_active', 'is_done', 'is_comment')


class CommentInformativeForm(forms.ModelForm):
    class Meta:
        model = CommentInformative
        exclude = ('user', 'informative', 'is_done', 'is_active')
