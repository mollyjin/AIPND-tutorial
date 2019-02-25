#!/usr/bin/python
# -*- coding:utf-8 -*-

import builtins

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))

print(hand)

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()