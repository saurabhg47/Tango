from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Rango is saying Hello!!!! to Tango")
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'about_rango': "Hey this page will give you the info about rango"}
    return render(request, 'rango/about.html', context_dict)
