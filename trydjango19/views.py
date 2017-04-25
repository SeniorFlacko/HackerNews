from django.shortcuts import render

def home(request):
    html="<h1>hola mundo</h1>"
    return render(request,html, {})