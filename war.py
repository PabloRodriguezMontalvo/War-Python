"""Initiate the War Game """

import deck_class
import player_class
import game_class

player1= player_class.Player()
player2=player_class.Player()
gameDeck=deck_class.Deck()
Mygame= game_class.Game(player1,player2,gameDeck)

Mygame.play_game()
