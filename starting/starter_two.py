class Animal:

    def __init__(self, name, weight, sound):
        self._name = name
        self.weight = weight
        self.sound = sound

    def set_name (self, name):
        self.name = name

    def set_sound (self, weight):
        self.weight = weight

    def set_sound (self, sound):
        self.sound = sound

    def get_name (self):
        return self.name

    def get_sound (self):
        return self.sound

    def get_weight (self):
        return self.wight

    def toString (self):
        return f"{self._name} says {self.sound}"

pityu = Animal ("Pityu", 2, "csirip")
print (pityu.toString())

class Bird (Animal):

    def __init__(self, name, weight, sound, gender):
        super().__init__(name, weight, sound)
        self.gender = gender

tomi = Bird ("Tomi", 3, "kurururu", "male")
print (tomi.toString())