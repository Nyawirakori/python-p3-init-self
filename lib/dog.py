#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):# init should always double underscores
        self.name = name
        self.breed = breed

fido = Dog("fido")
print(fido.breed)
