# Write a Python program that demonstrates inheritance by creating a base class Animal and derived classes like Dog, Cat.
class Animal:
 def __init__(self, name):
 self.name = name
 def eat(self):
 print(f"{self.name} is eating.")
class Dog(Animal):
 def bark(self):
 print(f"{self.name} is barking.")
class Cat(Animal):
 def meow(self):
 print(f"{self.name} is meowing.")
d = Dog("Buddy")
c = Cat("Whiskers")
d.eat()
d.bark()
c.eat()
c.meow() 
