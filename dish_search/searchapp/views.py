import csv
from django.shortcuts import render
from django.http import JsonResponse
import json
# from searchapp.models import Dish

# Create your views here.
def search(request):
    query = request.GET.get('query')
    if query:
        with open('restaurants_small.csv', 'r') as file:
            reader = csv.reader(file)
            # dishes = [row[1] for row in reader if query.lower() in row[1].lower()]
            dishes = []
            file.seek(0)
            reader2 = csv.reader(file)
            next(reader2)
            for row in reader2:
                temp_arr = [{'item':item ,'res': row[1]} for item in json.loads(row[3]) if query.lower() in item.lower()]
                dishes = dishes + temp_arr

    else:
        query = ""
        dishes = []
    
    return render(request, 'search.html', {'dishes': dishes, 'query': query})

