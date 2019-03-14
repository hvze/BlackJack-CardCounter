import numpy as np


# number of decks to be shuffled
def number_of_decks_():
    print('Number of Decks\n')
    _deck = True
    while _deck:
        try:
            _deck = int(input())
            return _deck
        except ValueError:
            print("Entry not valid")


# find value of specific card
def find_value(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    if card == 'A':
        return 'A'
    return int(card)


# find TRUE count of specific card
def find_true_count(card):
    card = find_value(card)
    if card == 'A' or card == 10:
        return -1
    elif 7 <= card <= 9:
        return 0
    elif card < 7:
        return 1


# creates decks
def create_decks():
    global cards
    global card_value
    global card_suit
    global shoe_penetration

    shoe_penetration = False
    number_of_decks = 6
    cards = []
    card_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suit = ['S', 'C', 'H', 'D']

    for decks in range(number_of_decks):
        for card_s in card_suit:
            for card_v in card_value:
                cards.append([decks, card_s, card_v])

    np.random.shuffle(cards)
    card_penetrated = int(len(cards) * np.random.randint(70, 75) / 100)
    cards.insert(card_penetrated, 'penetration')

    return cards


# deals the cards
def deal(true_count):
    global shoe_penetration

    shoe_penetration = False
    bet_r = 0
    cards_dealt = cards
    bet_big = False
    decks_remaining = len(cards_dealt) / 52

    if len(cards_dealt) > 0:

        top_card = cards_dealt.pop(0)

        if top_card == 'penetration':
            shoe_penetration = True
            top_card = cards_dealt.pop(0)

        true_count += find_true_count(top_card[2])

        if (true_count / decks_remaining) > (true_count / decks_remaining):
            bet_big = True
            bet_r = true_count / decks_remaining
        return top_card, shoe_penetration, true_count, bet_big, int(bet_r)


# number of players
def number_of_players():
    print('Number of Players\n')
    num_player = True
    while num_player:
        try:
            num_player = int(input())
            return num_player
        except ValueError:
            print("Entry not valid")


# creates lists of players
def player_hand():
    global players

    players = {'Dealer': []}
    # num_players = number_of_players()
    num_players = 1
    for player in range(num_players):
        players[' '.join(['Player', str(player + 1)])] = []

    return players


# creates lists of players with their money
def players_bank(num):

    global player_bank
    player_bank = {}

    for player in range(num):
        player_bank[' '.join(['Player', str(player + 1)])] = 10000

    return player_bank


# place bet amount
def bet_amount(bank):
    print('Place your bet\n')
    bet = True
    while bet:
        try:
            bet = int(input())
            if bet > bank:
                print('Insufficient Funds, try again')
            elif bet < 50:
                print('Please bet more than 50')
                bet = True
            else:
                return bet
        except ValueError:
            print("Entry not valid")


# number of players
def hit_or_stay():
    print('Press Enter or h to Hit or Press s to Stay')
    hit = True
    while hit:
        try:
            hit = input()
            if hit == 'h'or not hit:
                return True
            if hit == 's':
                return False
            else:
                print("Entry not valid")
        except ValueError:
            print("Entry not valid")


# checks which players have busted and if they beat the dealer
def check_round(play, bank):
    for player, card in play.items():
        if player == 'Dealer':
            if card == 'Bust':
                comp = 0
            else:
                comp = card
        if card == 'Bust':
            print(player, 'busted')
        elif player != 'Dealer' and card != 'Bust':
            if int(comp) == int(card):
                print(player, 'push with', card, 'and has', bank[player], 'Dollars')
            elif int(comp) < int(card):
                print(player, 'beat the dealer with', card, 'and has', bank[player], 'Dollars')
            else:
                print(player, 'lost to the dealer with', card, 'and has', bank[player], 'Dollars')
        else:
            print(player, 'has', comp)
