from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Help Desk Analyst Progress Tracker",
        "current_week_title": "Current Week",
        "previous_weeks_title": "Previous Weeks"
    }
    return render(request, "index.html", context)
