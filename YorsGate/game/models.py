from random import randint

from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    nickname = models.TextField(max_length=16)
    money = models.IntegerField(default=0)
    warehouse_capacity = models.IntegerField(default=100)
    reputation = models.IntegerField(default=50)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.nickname}| " \
               f"Money: {self.money}| " \
               f"Warehouse: {self.warehouse_capacity}| " \
               f"Reputation {self.reputation}"


class Ware(models.Model):
    product_name = models.TextField()
    price = models.IntegerField(default=0)
    time_of_sale = models.TimeField()
    product_volume = models.IntegerField()

    def __str__(self):
        return f"Name: {self.product_name}|" \
               f" Price: {self.price}|" \
               f" Volume: {self.product_volume}|" \
               f" Time of sale: {self.time_of_sale}|"


class Warehouse(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"Merchant: {self.player.nickname}|  Ware: {self.ware.product_name}"
