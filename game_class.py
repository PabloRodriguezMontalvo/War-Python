"""Gestiona la lógica del juego"""

class Game:
    """Class Game. Recibe los jugadores que van a jugar y el mazo de cartas"""

    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.deck.shuffle()

    def deal_cards(self):
        """Reparte las cartas a los dos jugadores"""
        while len(self.deck.deck) > 0:
            self.player1.add_card(self.deck.draw_card())
            self.player2.add_card(self.deck.draw_card())
        print("Se están repartiendo las cartas")

    def play_round(self):
        """Lógica en la que se roban las cartas y se decide quien ha ganado"""

        print(f"Al jugador 1 le quedan {len(self.player1.hand)} cartas")
        print(f"Al jugador 2 le quedan {len(self.player2.hand)} cartas")

        card1 = self.player1.hand.pop(0)
        card2 = self.player2.hand.pop(0)
        print(f"El jugador 1 juega {card1[1]} de {card1[0]}")
        print(f"El jugador 2 juega {card2[1]} de {card2[0]}")

        if card1[2] > card2[2]:
            self.player1.hand.append(card1)
            self.player1.hand.append(card2)
            print("El jugador 1 gana")

        elif card1[2] < card2[2]:
            self.player2.hand.append(card1)
            self.player2.hand.append(card2)

            print("El jugador 2 gana")
        else:
            self.war(card1, card2)

    def war(self, card1, card2):
        """Si dos cartas son iguales empieza la guerra. 
        Se ponen 3 cartas boca abajo y la cuarta (boca arriba) 
        decide quien se lleva todas las cartas"""
        print("Guerra!")
        if len(self.player1.hand) < 4 or len(self.player2.hand) < 4:
            return

        face_down_a1 = self.player1.hand.pop(0)
        face_down_b1 = self.player2.hand.pop(0)
        face_down_a2 = self.player1.hand.pop(0)
        face_down_b2 = self.player2.hand.pop(0)
        face_down_a3 = self.player1.hand.pop(0)
        face_down_b3 = self.player2.hand.pop(0)
        face_up1 = self.player1.hand.pop(0)
        face_up2 = self.player2.hand.pop(0)

        if face_up1[2] > face_up2[2]:
            self.player1.hand.extend([card1, card2, face_down_a1,
                                      face_down_a2, face_down_a3,
                                      face_down_b1, face_down_b2,
                                      face_down_b3, face_up1, face_up2])
        elif face_up1[2] < face_up2[2]:
            self.player2.hand.extend([card1, card2, face_down_a1,
                                      face_down_a2, face_down_b1, face_down_b2,
                                      face_down_b3, face_up1, face_up2])
        else:
            self.war(face_up1, face_up2)

    def play_game(self):
        """Iniciador del juego"""

        self.deal_cards()

        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            self.play_round()

        if len(self.player1.hand) > 0:
            print("¡El jugador 1 gana la partida!")
        else:
            print("¡El jugador 2 gana la partida!")
