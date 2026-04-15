from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start a daily journaling habit (5 minutes a day).",
    "february": "Do 20 minutes of movement 3× per week.",
    "march": "Learn one new Python concept and build a tiny demo.",
    "april": "Declutter one small area each week (desk, drawer, etc.).",
    "may": "Read 10 pages (or 15 minutes) a day.",
    "june": "Try cooking one new recipe each week.",
    "july": "Go for a 10-minute walk outside every day.",
    "august": "Practice a skill (typing, guitar, drawing) for 15 minutes a day.",
    "september": "Build a small Django feature (one form + one model).",
    "october": "No social media after 9 PM for the whole month.",
    "november": "Write down 3 things you’re grateful for every day.",
    "december": "Reach out to one person each week to reconnect.",
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'index.html', {'months': months})


def challenge_by_number(request, number):
    months = list(monthly_challenges.keys())
    if number > len(months):
        return HttpResponseNotFound("Invalid month")
    month = months[number - 1]
    return HttpResponseRedirect(reverse("challenges", args=[month]))

def challenge_by_month(request, month):
    if month not in monthly_challenges:
        return HttpResponseNotFound("Oops could\'nt find it")
    else:
        return HttpResponse(monthly_challenges[month])

