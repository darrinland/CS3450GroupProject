from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

# Create your views here.

def index(request) :
    template=loader.get_template("patient/index.html")
    return HttpResponse(template.render({}, request))