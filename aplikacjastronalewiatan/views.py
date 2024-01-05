from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def o_nas(request):
    return render(request, "o_nas.html")
def kontakt(request):
    return render(request, "kontakt.html")
def usługi(request):
    return render(request, "usługi.html")
