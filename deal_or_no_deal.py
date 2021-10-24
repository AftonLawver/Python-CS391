# Create a class that creates suitcases for deal or  no deal game

class Suitcase():
    
    def __init__(self, name: str, isOnBoard = True):
        self.name = name

    def delete_isOnBoard(self):
        self.isOnBoard = False

    def set_amount(self, amount):
        self.amount = amount
    
    def get_amount(self):
        return self.amount
    
    def get_name(self):
        return self.name

