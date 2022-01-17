from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



monthly_challenges = {
    "january": "First Month of the year!",
    "fabruary": "2nd Month of the year!",
    "march": "3 Month of the year!",
    "april": "4 Month of the year!",
    "may": "5 Month of the year!",
    "june": "6 Month of the year!",
    "july": "7 Month of the year!",
    "august": "8 Month of the year!",
    "september": "9 Month of the year!",
    "october": "10 Month of the year!",
    "november": "11 Month of the year!",
    "december": "12 Month of the year!",
}


# Create your views here.

def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invlid Month')
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def month_challenges(request, month):
    try:
        challenges_txt = monthly_challenges[month],
        return HttpResponse(challenges_txt)
    except:
        return HttpResponseNotFound("This Page is not Supported")
