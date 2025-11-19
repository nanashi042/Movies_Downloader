# views.py

from django.shortcuts import render
from Moviesnation_scrape.utils import Moviesnation_scrape
import logging

logger = logging.getLogger(__name__)

def mov(request):
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        results = Moviesnation_scrape.moviename(query)

        return render(request, "movie.html", {
            "results": results,
            "query": query
        })

    return render(request, "movie.html")


def home(request):
    return  render(request, "home.html")