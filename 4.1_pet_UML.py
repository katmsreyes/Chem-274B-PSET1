#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 16:54:01 2025

@author: katrinareyes
"""

class Meal:
    def __init__(self, taste, weight):
        self. taste = taste
        self. weight = weight        


class Pet:
    def __init__(self, name):
        self. name = name;
        
    def makeSound(self, sound):
        print(sound)
        
    def eat(self, name, food):
        if isinstance(food, Meal):
            print(f'{self.name} eats {food}.')
            

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return f'super().__init__() Dog Name: {self.name}'

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return f'super().__init__() Cat Name: {self.name}'
    
class Mouse(Pet):
    def __init__(self, name):
        super().__init__(name)
    def __repr__(self):
        return f'super().__init__() Mouse Name: {self.name}'

class Person :
    def __init__(self, counter, ID, firstName, lastName):
        self.counter = counter
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        
        self.pets_owned = []
    def adopt_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets_owned.append[pet]
            
