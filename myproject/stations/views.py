from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render
from .models import BusStation
import pandas as pd

def bus_stations(request):
    csv_path = settings.BUS_STATION_CSV

    
    BusStation.objects.all().delete()
    data = pd.read_csv(csv_path)

    selected_columns = ['Name', 'Street', 'AdmArea']
    data = data[selected_columns]

    for _, row in data.iterrows():
        BusStation.objects.create(
            name=row['Name'],
            location=row['Street'],
            district=row['AdmArea']
        )

    page_number = request.GET.get('page')
    paginator = Paginator(BusStation.objects.all(), per_page=10)  

    page = paginator.get_page(page_number)

    return render(request, 'stations/bus_stations.html', {'page': page})
