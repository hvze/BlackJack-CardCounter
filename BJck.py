import Functions as fn

cards = fn.create_decks()
players = fn.player_hand()
player_bank = fn.players_bank(len(players) - 1)


def play_round():

    shoe_penetration = False
    play = True
    round_in_play = True
    board = []
    dealt = False
    num_rounds = 0
    num_hands = 0
    tc = 0
    bb = 0
    br = 0
    bj = False

    while play:

        if not dealt and round_in_play:

            # clears the player's hands

            for player, card in players.items():
                players[player] = []

            # draws the first two cards for each of the players
            for draw_cards in range(2):
                for turn in players:
                    hand = fn.deal(tc)
                    tc, bb, br = hand[2], hand[3], hand[4]
                    num_hands += 1
                    if hand[1]:
                        shoe_penetration = True
                        print('____________________________________________________________________________________')
                    board.append([turn, hand[0]])
                    hand = fn.find_value(hand[0][2])
                    if hand == 'A':
                        players[turn].append([1, 11])
                    else:
                        players[turn].append(hand)
            # print(players)
            # finds out value of hand
            for player, card in players.items():
                if [1, 11] in card:
                    if card[0] == [1, 11] and card[1] == [1, 11]:
                        players[player] = [2, 12]
                    elif card[0] != [1, 11]:
                        card1 = card[0] + 1
                        card2 = card[0] + 11
                        players[player] = [card1, card2]
                    else:
                        card1 = card[1] + 1
                        card2 = card[1] + 11
                        players[player] = [card1, card2]
                else:
                    players[player] = sum(card)

            # print(board)
            # print(players)
            print()
            dealer_in_play = True
            player_num = 1
            bet_done = True
            bet_amount = 5

            # play the game
            while dealer_in_play:

                for player_in_play, card_in_play in players.items():

                    # get current player
                    current_player = ' '.join(['Player', str(player_num)])
                    # asks for bet amount
                    if bet_done:
                        # player_bank[current_player] -= fn.bet_amount(player_bank[current_player])
                        if player_bank[current_player] > 0:
                            if bb:
                                player_bank[current_player] -= bet_amount * br
                                print(player_bank, 'bet was big___________with ', bet_amount * br, '_____________', tc)
                                bet_done = False
                            else:
                                player_bank[current_player] -= bet_amount
                                print(player_bank)
                                bet_done = False
                        else:
                            print('Player is broke')
                            return num_rounds, num_hands, player_bank
                    # checks if it's player or dealer
                    if player_in_play == current_player:

                        # creates new hand
                        player_hand = card_in_play
                        print(player_in_play, 'turn to play with', player_hand, 'in hand with', bet_amount, 'bet.')
                        print(players)
                        # check to see if player hits or stays
                        # dealer_in_play = fn.hit_or_stay()
                        if type(player_hand) == list:
                            if player_hand[1] < 17:
                                dealer_in_play = True
                            else:
                                if player_hand[1] == 21:
                                    bj = True
                                dealer_in_play = False
                        elif player_hand < 12:
                            dealer_in_play = True
                        elif player_hand > 11:
                            dealer_in_play = False

                        # player hits
                        if dealer_in_play:
                            print('Player', str(player_num), 'has hit')
                            hand = fn.deal(tc)
                            tc, bb, br = hand[2], hand[3], hand[4]
                            num_hands += 1
                            if hand[1]:
                                shoe_penetration = True
                                print('____________________________________________________________________________')
                            board.append([player_in_play, hand[0]])
                            hand = fn.find_value(hand[0][2])

                            # checks if an Ace is drawn
                            if hand == 'A':

                                print('Player', str(player_num), 'drew an', hand, '\n')

                                # if an Ace is already in hand
                                if type(player_hand) == list:
                                    card1_in_play = player_hand[0] + 1
                                    card2_in_play = player_hand[1] + 1
                                    if card2_in_play > 21:
                                        players[player_in_play] = card1_in_play
                                        print(current_player, 'has', card1_in_play, '\n')
                                    else:
                                        players[player_in_play] = [card1_in_play, card2_in_play]
                                        print(current_player, 'has', card1_in_play, card2_in_play, '\n')

                                # no Ace in hand
                                else:

                                    if int(player_hand) > 10:
                                        player_hand += 1
                                        if int(player_hand) > 21:
                                            print(current_player, 'Bust with', player_hand, '\n')
                                            players[player_in_play] = 'Bust'
                                            player_num += 1
                                        else:
                                            print(current_player, 'has', player_hand, '\n')
                                            players[player_in_play] = player_hand

                                    elif int(player_hand) <= 10:
                                        players[player_in_play] = [int(player_hand) + 1, int(player_hand) + 11]

                            # if no Ace is drawn
                            else:
                                print('Player', str(player_num), 'drew a', hand, '\n')

                                # if an Ace is already in hand
                                if type(player_hand) == list:
                                    card1_in_play = player_hand[0] + hand
                                    card2_in_play = player_hand[1] + hand
                                    if card2_in_play > 21:
                                        players[player_in_play] = card1_in_play
                                        print(current_player, 'has', card1_in_play, '\n')
                                    else:
                                        players[player_in_play] = [player_hand[0] + hand, player_hand[1] + hand]
                                        print(current_player, 'has', card1_in_play, card2_in_play, '\n')

                                # if no Ace in hand
                                else:
                                    player_hand += hand
                                    if int(player_hand) > 21:
                                        print(current_player, 'Bust with', player_hand, '\n')
                                        players[player_in_play] = 'Bust'
                                        player_num += 1

                                    elif int(player_hand) <= 21:
                                        players[player_in_play] = player_hand

                            print(players)

                        # if Player chose to stay
                        else:

                            # with an Ace chooses highest value
                            if type(player_hand) == list:
                                players[player_in_play] = player_hand[1]
                                print('player chose to stay with', player_hand[1], '\n')
                                bet_done = True

                            # no Ace
                            else:
                                print('player chose to stay with', player_hand, '\n')
                                bet_done = True

                            print(players)
                            player_num += 1

                        # all players have played and dealer starts their turn
                        if player_num >= len(players):
                            all_players = True
                            dealer_on = True
                            print('Dealer Plays')

                            # checks which players busted
                            for player, card in players.items():
                                if card != 'Bust' and player != 'Dealer':
                                    all_players = False
                                    print(player, 'in play with', card)

                            # if all players busted then exit round, if not then dealer plays
                            if all_players:
                                print('All players busted')
                                dealer_on = False
                                dealer_in_play = False

                            if dealer_on:

                                while dealer_on:

                                    dealer_hand = players.get('Dealer')

                                    # if dealer has an ace in hand
                                    if type(dealer_hand) == list:
                                        dealer_hand1 = dealer_hand[0]
                                        dealer_hand2 = dealer_hand[1]
                                        if dealer_hand2 > 21:
                                            players['Dealer'] = dealer_hand1
                                        elif 17 <= dealer_hand1 <= 21:
                                            players['Dealer'] = dealer_hand1
                                            print('Dealer stays with', dealer_hand1)
                                            dealer_on = False
                                        elif 17 <= dealer_hand2 <= 21:
                                            players['Dealer'] = dealer_hand2
                                            print('Dealer stays with', dealer_hand2)
                                            dealer_on = False
                                        else:
                                            dealer_draw = fn.deal(tc)
                                            tc, bb, br = dealer_draw[2], dealer_draw[3], dealer_draw[4]
                                            num_hands += 1
                                            print(dealer_draw)
                                            if dealer_draw[1]:
                                                shoe_penetration = True
                                                print('________________________________________')

                                            # draws a card a finds the value
                                            dealer_draw = fn.find_value(dealer_draw[0][2])

                                            # dealer draws an ace
                                            if dealer_draw == 'A':
                                                if dealer_hand1 <= 10:
                                                    dealer_hand1 = dealer_hand[0] + 11
                                                    players['Dealer'] = dealer_hand1
                                                else:
                                                    dealer_hand1 = dealer_hand[0] + 1
                                                    players['Dealer'] = dealer_hand1

                                                dealer_hand2 = dealer_hand[1] + 1
                                                players['Dealer'] = dealer_hand2
                                            else:
                                                dealer_hand1 = dealer_hand[0] + dealer_draw
                                                dealer_hand2 = dealer_hand[1] + dealer_draw
                                                players['Dealer'] = [dealer_hand1, dealer_hand2]
                                                print(players['Dealer'])

                                    # if no ace in hand
                                    else:

                                        if int(dealer_hand) < 17:

                                            dealer_draw = fn.deal(tc)
                                            tc, bb, br = dealer_draw[2], dealer_draw[3], dealer_draw[4]
                                            num_hands += 1
                                            print(dealer_draw)
                                            if dealer_draw[1]:
                                                shoe_penetration = True
                                                print('________________________________________')
                                            dealer_draw = fn.find_value(dealer_draw[0][2])
                                            print('Dealer draws a', dealer_draw)
                                            if dealer_draw == 'A':
                                                if int(dealer_hand) <= 10:
                                                    dealer_hand += 11
                                                    players['Dealer'] = dealer_hand
                                                    print(players['Dealer'], players.get('Dealer'))
                                                else:
                                                    dealer_hand += 1
                                                    players['Dealer'] = dealer_hand
                                                    print(players['Dealer'], players.get('Dealer'))

                                            else:
                                                dealer_hand += dealer_draw
                                                players['Dealer'] = dealer_hand

                                        # Dealer has 17 - 21 and stays
                                        if 17 <= int(dealer_hand) <= 21:

                                            print('Dealer stays with', dealer_hand)
                                            dealer_on = False

                                            for player, card in players.items():
                                                if card != 'Bust' and player != 'Dealer':
                                                    if card == dealer_hand:
                                                        player_bank[player] += bet_amount
                                                        print(player, 'push with', bet_amount)
                                                    elif card > dealer_hand:
                                                        if bj:
                                                            player_bank[player] += (bet_amount * 2) + (bet_amount/2)
                                                            print(player, 'beat the dealer with '
                                                                          ' a BlackJack and won',
                                                                  (bet_amount * 2) + (bet_amount/2))
                                                            bj = False
                                                        else:
                                                            player_bank[player] += bet_amount * 2
                                                            print(player, 'beat the dealer and won', bet_amount * 2)
                                                    else:
                                                        print('Dealer beat', player)

                                        # Dealer has over 21 and busts
                                        elif int(dealer_hand) > 21:

                                            print('Dealer has busted with ', dealer_hand)
                                            players['Dealer'] = 'Bust'
                                            dealer_on = False

                                            for player, card in players.items():
                                                if card != 'Bust' and player != 'Dealer':
                                                    player_bank[player] += bet_amount * 2
                                                    print(player, 'beat the dealer and won', bet_amount * 2)

            # shoe_penetration = True

        if shoe_penetration:
            cards = fn.create_decks()
            tc = 0
            bb = 0
            print('tc has been reset------------------------------------------round is over\n')
            num_rounds += 1
            print(num_rounds)
            shoe_penetration = False
            if num_rounds > 99:
                return num_rounds, num_hands, player_bank


result = play_round()
# fn.check_round(players, player_bank)
print('Player played', result[0], 'rounds and played', result[1], 'hands with', result[2].get('Player 1'), 'in the bank')


# print(result[2].get('Player 1'))

exit()
# TODO (make bets)(auto-play with basic strategy) (statistics)--------
