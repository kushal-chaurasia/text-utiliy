from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):



    djText=(request.GET.get('text', 'default'))
    remPunc=(request.GET.get('removePunctuations', 'off'))
    upperCase = (request.GET.get('capital', 'off'))
    newLine = (request.GET.get('newLine', 'off'))

    if remPunc =="on":
        Punctuations = ''',.?'";:#%^&*)('''
        analyzed = ""
        for char in djText:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzedText':analyzed}
        return render(request, 'analyze.html', params)

    elif upperCase == "on":
        analyzed = djText.upper()
        params = {'purpose': 'Capitalization', 'analyzedText':analyzed}
        return render(request, 'analyze.html', params)
    
    elif newLine=="on":
        analyzed=""
        for char in djText:
            if char != "\n":
                analyzed= analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzedText':analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("error")

def contactus(request):
    return HttpResponse("contact us")

def aboutus(request):
    return HttpResponse(aboutus)