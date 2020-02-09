from django.http import HttpResponse
from django.template import loader

def index(request):
    doc_externo = loader.get_template('index.html')
    render = doc_externo.render({"":""})
    return HttpResponse(render)

def about (request):
    doc_externo = loader.get_template('about.html')
    render = doc_externo.render({"":""})
    return HttpResponse (render)