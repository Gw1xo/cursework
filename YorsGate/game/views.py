from random import random
from typing import Dict, Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from json import loads

from .models import Ware


# Views == Controller
@login_required
def merchant(request):
    if not Player.objects.filter(id=request.user.id).exists():
        Player.objects.create(nickname=request.user.username,
                              user_id=request.user.id)

    player = Player.objects.get(id=request.user.id)
    wares = Ware.objects.all()

    context = {
        "title": 'Порт Йорсу',
        "user_id": request.user.id,
        "player": player,
        "wares": wares,
    }

    return render(request, 'game/merchant.html', context=context)


@login_required()
def warehouse_append(request):
    player = Player.objects.get(id=request.user.id)
    player_wares = Warehouse.objects.filter(player_id=request.user.id)

    if request.method == "POST":
        wares = loads(request.body)
        order_sum = 0
        for ware in wares:
            if ware['count'] > 0:
                if len(player_wares.filter(ware_id=ware['ware'])) > 0:
                    player_wares.filter(ware_id=ware['ware']).update(count=F('count') + ware['count'])
                    print(player_wares.get(ware_id=ware['ware']).count)
                else:
                    player_wares.create(player_id=request.user.id, ware_id=ware['ware'], count=ware['count'])
                order_sum += ware['price']

        player.money -= order_sum
        player.save()

    order_volume = 0
    max_capacity = 100 + (player.reputation / 10) * 4

    for ware in player_wares:
        order_volume += ware.ware.product_volume

    player.warehouse_capacity = max_capacity - order_volume
    player.save()

    context = {
        'title': 'Склад',
        "player": player,
        'wares': player_wares,
        'wares_volume': order_volume,
        'capacity': max_capacity
    }

    return render(request, 'game/warehouse.html', context=context)


@login_required()
def shop(request):
    player = Player.objects.get(id=request.user.id)
    player_wares = Warehouse.objects.filter(player_id=request.user.id).order_by('ware_id')

    if request.method == "POST":
        sell_wares = loads(request.body)
        sell_sum = 0
        for ware in sell_wares:
            sell_ware = Warehouse.objects.get(player_id=request.user.id, ware_id=ware['id'])
            if ware['count'] < sell_ware.count:
                sell_sum += ware['count'] * sell_ware.ware.price
                sell_ware.count -= ware['count']
                sell_ware.save()
            else:
                sell_sum += sell_ware.count * sell_ware.ware.price
                sell_ware.delete()

            player.money += sell_sum + (player.reputation - 50)

    context = {
        'title': 'Ваш магазин',
        'player': player,
        'player_wares': player_wares,
    }

    return render(request, 'game/shop.html', context=context)

