from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def courses(request):
    return render(request, 'courses.html')

def notes(request):
    return render(request, 'notes.html')

def performance(request):
    return render(request, 'performance.html')
