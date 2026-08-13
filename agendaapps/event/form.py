from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import TypeAgenda, CatAgenda, Agenda,AgendaRecipient, RequestAgenda, Informative, CommentInformative
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from django_summernote.widgets import SummernoteWidget


class TypeAgendaForm(forms.ModelForm):
    class Meta:
        model = TypeAgenda
        exclude = ('id',)
        
class CategoryAgendaForm(forms.ModelForm):
    class Meta:
        model = CatAgenda
        exclude = ('id',)

class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda

        exclude = (
            'title_slug',
            'is_cancel',
            'is_active',
            'status',
            'observation',
        )

        widgets = {
            "start_time": DateTimePickerInput(),

            "end_time": DateTimePickerInput(
                range_from="start_time"
            ),

            "recipients": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["recipients"].queryset = (
            AgendaRecipient.objects
            .filter(is_active=True)
            .order_by("position", "name")
        )
        
        
class AgendaRecipientForm(forms.ModelForm):

    class Meta:
        model = AgendaRecipient

        fields = [
            "name",
            "position",
            "email",
            "is_default",
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Naran kompletu",
                }
            ),

            "position": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ez: Director, Minister",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "email@example.com",
                }
            ),

            "is_default": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

class PostponedAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ('title_slug', 'invitedinstitue',
                   'is_cancel', 'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),

        }

        
class CommentAgendaForm(forms.ModelForm):

    observation = forms.CharField(
        widget=SummernoteWidget(
            attrs={
                'placeholder': 'Observasaun'
            }
        ),
        required=False,
        label="OBSERVASAUN"
    )

    attachment = forms.FileField(
        required=False,
        label='DOKUMENTU'
    )

    class Meta:
        model = Agenda
        fields = [
            'attachment',
            'observation'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.enctype = 'multipart/form-data'

        self.helper.layout = Layout(
            Row(
                Column(
                    'attachment',
                    css_class='form-group col-md-6 mb-3'
                ),
                Column(
                    'observation',
                    css_class='form-group col-md-6 mb-3'
                ),
                css_class='form-row'
            )
        )   
        


class RequestedAgendaForm(forms.ModelForm):
    class Meta:
        model = RequestAgenda
        exclude = ('title_slug',
                   'is_active', 'status', 'observation')
        widgets = {
            "start_time": DateTimePickerInput(),
            "end_time": DateTimePickerInput(range_from="start_time"),
        }


class InformativeForm(forms.ModelForm):
    class Meta:
        model = Informative
        exclude = ('title_slug', 'observation',
                   'is_active', 'is_done', 'is_comment')


class CommentInformativeForm(forms.ModelForm):
    class Meta:
        model = CommentInformative
        exclude = ('informative', 'is_done', 'is_active')
        



