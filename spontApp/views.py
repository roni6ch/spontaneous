from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from amadeus import Flights
import datetime
import math
# logging:
import logging
logger = logging.getLogger('spontApp')


# Create your views here.

AMADEUS_API_KEY = 'ikb2WCbOOrKkFf5biRa1GmuoGObAz9L7'
NUM_DAYS_FROM_NOW = 7
DATE_FORMAT = '%Y-%m-%d'


@require_GET
def index(request):
    return render(request, 'index.html', {})


@require_POST
def query(request):
    # get params:
    budget = int(request.POST["budget"])
    origin = request.POST["origin"]
    num_passengers = int(request.POST["num_passengers"])

    # calc departure_date - 7 days from now:
    today = datetime.datetime.now()
    x_days_after = today + datetime.timedelta(days=NUM_DAYS_FROM_NOW)
    departure_date = '%s--%s' % (today.strftime(DATE_FORMAT), x_days_after.strftime(DATE_FORMAT))
    logger.debug(departure_date)
    # calc max price:
    max_price = int(budget / num_passengers)
    logger.debug(type(max_price))

    # query amadeus:
    flights = Flights(AMADEUS_API_KEY)
    resp = flights.extensive_search(
        origin=origin,
        destination='LAX',
        departure_date=departure_date,
        max_price=budget)

    # TODO: remove flights with less seats then needed - can't

    return JsonResponse(data=resp, status=200)
