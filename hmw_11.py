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
        self.bank = Bank(bank)
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
                return card.balance - sum


    def add(self, card, sum):
        card = card.balance
        return card + sum

    def change_pin(self, card, old_pin, new_pin):
        card = card.pin
        if card.pin == old_pin:
            card.pin = new_pin
            return card


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = set()

    def open_account(self, client):
        account = Client(client)
        card = Card(random.randint(10000, 99999), 0.0, 0000, account, self.name,)
        account.cards.append(card)
        return self.accounts.add(account)

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


client = Client("John")
bank = Bank("PrivatBank")
atm = ATM(bank, 10000)

card = bank.open_account(client)
assert card.balance == 0.0

atm.add(card, 500)
assert card.balance == 500.0

