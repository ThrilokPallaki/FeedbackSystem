# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Questions, Answers, Users
# Register your models here.

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Users)
