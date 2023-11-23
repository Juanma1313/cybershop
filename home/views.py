from django.shortcuts import render


def index(request):
    """ View to return the index page """
    print("user={}".format(request.user))
    return render(request, 'home/index.html')
