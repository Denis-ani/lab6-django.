from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Ласкаво просимо на сайт!</h1>")

