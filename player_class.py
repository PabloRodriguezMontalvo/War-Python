"""Gestiona la funcionalidad de los jugadores, un jugador tiene una mano de cartas y puede robar más"""
import random

class Player:
    """Represents a player in a card game."""

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        """Añade una carta a la mano"""
        self.hand.append(card)

    def shuffle(self):
        """Baraja la mano"""
        random.shuffle(self.hand)
