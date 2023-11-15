from django.shortcuts import render


def home(request):
    # return HttpResponse("Hi , working")
    return render(request, 'webapp/index.html')
