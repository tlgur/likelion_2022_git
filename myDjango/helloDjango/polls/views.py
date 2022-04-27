from django.shortcuts import render, HttpResponse

def index(request):
        return HttpResponse("Hello, Django!")

def create(req):
    return HttpResponse("Create")

def read(req, id):
    return HttpResponse("Read" + id)
