from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import TypeAgenda, CatAgenda, Agenda, AgendaDelegation, AgendaTo, AgendaRecipient, RequestAgenda, Informative, CommentInformative
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from django_summernote.widgets import SummernoteWidget


class TypeAgendaForm(forms.ModelForm):

    class Meta:
        model = TypeAgenda

        fields = [
            'name_type',
        ]

        labels = {
            'name_type': 'Tipu Ajenda',
        }

        widgets = {
            'name_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Hakerek Tipu Ajenda...',
                    'autocomplete': 'off',
                }
            ),
        }

    def clean_name_type(self):

        name_type = self.cleaned_data.get('name_type')

        if name_type:
            name_type = name_type.strip()

            queryset = TypeAgenda.objects.filter(
                name_type__iexact=name_type
            )

            # Important for EDIT
            if self.instance.pk:
                queryset = queryset.exclude(
                    pk=self.instance.pk
                )

            if queryset.exists():
                raise forms.ValidationError(
                    'Tipu Ajenda ida-ne\'e iha ona iha sistema.'
                )

        return name_type
        
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
            "central_user_id",
            "central_username",
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
        
        
class AgendaToForm(forms.ModelForm):

    class Meta:
        model = AgendaTo

        fields = [
            'code',
            'name',
            'is_active',
        ]

        labels = {
            'code': 'Kodigu',
            'name': 'Partisipante',
            'is_active': 'Ativu',
        }

        widgets = {
            'code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ezemplu: MN, VMN',
                    'autocomplete': 'off',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ezemplu: Ministro',
                    'autocomplete': 'off',
                }
            ),
        }

    def clean_code(self):
        code = self.cleaned_data.get('code')

        if code:
            code = code.strip().upper()

            queryset = AgendaTo.objects.filter(
                code__iexact=code
            )

            if self.instance.pk:
                queryset = queryset.exclude(
                    pk=self.instance.pk
                )

            if queryset.exists():
                raise forms.ValidationError(
                    'Kodigu ida-ne\'e iha ona iha sistema.'
                )

        return code

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            name = name.strip()

            queryset = AgendaTo.objects.filter(
                name__iexact=name
            )

            if self.instance.pk:
                queryset = queryset.exclude(
                    pk=self.instance.pk
                )

            if queryset.exists():
                raise forms.ValidationError(
                    'Partisipante ida-ne\'e iha ona iha sistema.'
                )

        return name
    

        
class AgendaDelegationForm(forms.ModelForm):

    class Meta:
        model = AgendaDelegation

        fields = [
            "delegated_to",
            "note",
        ]

        widgets = {
            "delegated_to": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "note": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Hakerek nota delegasaun..."
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Only Vice-Minister
        self.fields["delegated_to"].queryset = (
            AgendaTo.objects.filter(
                code="VMN",
                is_active=True
            )
        )

        self.fields["delegated_to"].empty_label = (
            "--- Hili Partisipante ---"
        )  
        
        
    
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
        



