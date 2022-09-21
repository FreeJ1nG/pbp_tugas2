from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def index(request):
  return HttpResponse()

def show_xml(request):
  return HttpResponse(
    serializers.serialize("xml", MyWatchList.objects.all()), 
    content_type="application/xml"
  )
  
def show_json(request):
  return HttpResponse(
    serializers.serialize("json", MyWatchList.objects.all()),
    content_type="application/json"
  )

def show_html(request):
  watchlist = MyWatchList.objects.all()
  watched = len(watchlist.filter(watched = True))
  unwatched = len(watchlist.filter(watched = False))
  return render(
    request,
    "mywatchlist.html",
    {
      "watchlist": watchlist,
      "watched": watched,
      "unwatched": unwatched,
    }
  )