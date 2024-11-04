from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('myapp/myfirst.html')
    # return HttpResponse("Hello wordl")
    # return HttpResponse(template.render())

class HomePageView(TemplateView):
    template_name = "myapp/myfirst.html"

class AboutPageView(TemplateView):
    template_name = "myapp/mysecond.html"