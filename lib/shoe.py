#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        
    def get_shoe_size(self):
        return self._size
    def set_shoe_size(self, value):
        if value is int:
            self._size = value
        else:
            print('size must be an integer') 
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


    size = property(get_shoe_size, set_shoe_size)

   