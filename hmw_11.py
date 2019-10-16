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
        # if self.bank != card.bank:
        #     print("This card is not valid")
        if sum > self.amount:
            print("Sorry, we don't have this amount of money")
        else:
            if sum > card.balance:
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

    # def show_total_balance(self):
    #     total = []
    #     for money in self.cards:
    #         if money == card.balance:
    #             total.append(money)
    #     return total


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
bank1= Bank("AlfaBank")
atm = ATM(bank, 10000)
wallet = Card(22222, 250.0, 0000, client, bank)
print(atm.withdraw(wallet, 20))

# print(client.show_total_balance())
card = bank.open_account(client)
assert card.balance == 0.0

atm.add(card, 500)
assert card.balance == 500.0

# Write a function called choose_func which takes a list of nums and 2
# callback functions. If all nums inside the list are positive, execute the
# first function on that list and return the result of it. Otherwise return the
# result of the second one


def choose_func(nums: list, func1, func2):
    for num in nums:
        if num > 0:
            a = func1(nums)
        else:
            b = func2(nums)
            return b
    return a


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]