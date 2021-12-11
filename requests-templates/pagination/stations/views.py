from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = list(reader)
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(CONTENT, 10)
        page = paginator.get_page(page_number)
            # получите текущую страницу и передайте ее в контекст
            # также передайте в контекст список станций на странице

        context = {
            'bus_stations': paginator.page(page_number).object_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
