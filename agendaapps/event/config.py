# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.apps import AppConfig


class MyConfig(AppConfig):
    name = 'agendaapps.event'
    label = 'agendaapps_event'
    
    def ready(self):
        import agendaapps.event.signals
