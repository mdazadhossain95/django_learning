from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
# from django.template.loader import render_to_string

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
    "december": None,
}


# Create your views here.

# showing html view in page
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,

    })


# number check
def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        rasponse_data = render_to_string("404.html")
        return HttpResponseNotFound(rasponse_data)

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])  # /challenges/
    return HttpResponseRedirect(redirect_path)


# String check
def month_challenges(request, month):
    try:
        challenges_txt = (monthly_challenges[month],)
        return render(request, "challenges/challenge.html", {
            "text": challenges_txt,
            "month_name": month.capitalize()
            })
    except:
        raise Http404()
