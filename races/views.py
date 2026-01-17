from django.shortcuts import render

def home_view(request):
    return render(request, "races/race_calendar.html")

