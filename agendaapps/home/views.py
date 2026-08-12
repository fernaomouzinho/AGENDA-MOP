from django.shortcuts import render
from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from agendaapps.event.models import Agenda


def index(request):
    
    context = {
        'segment': 'index'
    }
    
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
