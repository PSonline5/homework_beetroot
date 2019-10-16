import random
# Implement a simple composition of 4 classes: ATM, Client, Card, Bank
#
# Bank(name) + accounts = [] - list of all accounts opened in the current bank
# methods:
#   open_account(client: Client) - takes an instance of Client class as an
# argument and creates a new instance of Card bound to this client (and returns
# it). ! A client can only open one account per bank !
#   close_account(card: Card) - removes specified instance of Card
#
# ATM(bank: Bank, amount: float) - takes an instance of Bank class as an
# argument (the bank this card is bound to) and the amount of money in
# the current ATM.
# methods:
#   withdraw(card: Card, sum: float) - takes two arguments: an instance of
# Card and sum which is needed to be withdrawn. You should consider 2 cases:
#       1) when the amount of money in the bank is less than the sum
#       2) when the ATM and Card are bound to different banks (it shouldn't
# let you withdraw)
#   add(card: Card, sum: float) - add the specified amount of money to the card
#   change_pin(card: Card, old_pin: int, new_pin: int) - change card's pin
#
# Card(account: int, balance: float, pin: int, owner: Client, bank: Bank) -
# account is just a random 5-digit number. Pin is 0000 by default
# methods:
#   transfer_money(card, amount) - transfers the money from the current card to
# the specified one
#
# Client(name: str) + cards = [] - list of cards bound to the client
# methods:
#   show_total_balance - returns the sum of money from all cards owned by the
# client


class ATM:
    def __init__(self, bank, amount):
        self.bank = bank
        self.amount = amount

    def withdraw(self, card, sum):
        if sum > self.amount:
            print("Sorry, we don't have this amount of money")
        if self.bank not in card.bank:
            print("This card is not valid")
        else:
            if sum < card.balance:
                print("You can't withdraw this sum,try less")
            else:
                card.balance = card.balance - sum
                return card.balance

    def add(self, card, sum):
        card.balance = card.balance + sum
        return card.balance

    def change_pin(self, card, old_pin, new_pin):
        if card.pin == old_pin:
            card.pin = new_pin
            return card.pin


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = set()

    def open_account(self, client):
        card = Card(random.randint(10000, 99999), 0.0, 0000, client, self.name)
        client.cards.append(card)
        self.accounts.add(client)
        return card

    def close_account(self, card):
        self.accounts.remove(card)


class Client:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show_total_balance(self):
        self.cards = sum(card.balance)
        return self.cards


class Card:
    def __init__(self, account, balance, pin, owner, bank):
        self.account = account
        self.balance = balance
        self.pin = pin
        self.owner = Client(owner)
        self.bank = Bank(bank)

    def transfer_money(self, card, amount):
        self.balance = self.balance - amount
        card.balance = card.balance + amount
        return self.balance


client = Client("John")
bank = Bank("PrivatBank")
atm = ATM(bank, 10000)


card = bank.open_account(client)
assert card.balance == 0.0

atm.add(card, 500)
assert card.balance == 500.0

