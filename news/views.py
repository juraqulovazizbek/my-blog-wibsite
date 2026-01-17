from django.shortcuts import render

def home_view(request):
    return render(request, "news/news_list.html")
