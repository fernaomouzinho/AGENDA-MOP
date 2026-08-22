from django.shortcuts import render
from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from agendaapps.event.models import Agenda
from django.urls import reverse
from django.utils import timezone
from agendaapps.authentication.decorators import allowed_users
from agenda.utils import get_roles


@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user',
        'ajenda_vmn'
    ]
)
def index(request):
    roles = get_roles(request)
    
    context = {
        'segment': 'index',
        'roles':roles,
    }
    
    if "ajenda_vmn" in roles:
        
        html_template = loader.get_template('home/home2.html')
    else:
        html_template = loader.get_template('home/home1.html')
    return HttpResponse(html_template.render(context, request))
