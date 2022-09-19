from django.urls import path
from mywatchlist.views import (index, show_xml, show_json, show_html)

app_name = 'mywatchlist'

urlpatterns = [
  path('', index, name='index'),
  path('xml/', show_xml, name='show_xml'),
  path('json/', show_json, name='show_json'),
  path('html/', show_html, name='show_html'),
]