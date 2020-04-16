#!/usr/bin/python3




# 1)
class Animal: # 9)
    
    ZOO_NAME = 'Hayaton'
    
    def __init__(self, name):
        self._name = name
        self._hunger = 0
    
    def get_name(self):
        return self._name
    
    def is_hungry(self):
        return self._hunger > 0
    
    def feed(self):
        if self.is_hungry():
            self._hunger -= 1
            
    def talk(self):
        pass
    
    
# 2)
# 3)
class Dog(Animal):
    
    def talk(self):
        print('woof woof')
        
    def fetch_stick(self):
        print('There you go, sir!')

class Cat(Animal):
    
    def talk(self):
        print('meow')
    
    def chase_laser(self):
        print('Meeeeow')

# 7)
class Skunk(Animal):
    
    def __init__(self, name, stink_count=6):
        super().__init__(name)
        self._stink_count = stink_count
    
    def talk(self):
        print('tsssss')
    
    def stink(self):
        self._stink_count += 1
        print('Dear lord!')
        

class Unicorn(Animal):
    
    def talk(self):
        print('Good day, darling')
        
    def sing(self):
        print('i\'m not your toy....')

class Dragon(Animal):
    
    def __init__(self, name, color = 'Green'):
        super().__init__(name)
        self._color = color
        
    def talk(self):
        print('Raaaawr')
        
    def breath_fire(self):
        print('$@#$#@$')

# 4)
def main():
    brownie = Dog('Brownie')
    brownie._hunger = 10
    zelda = Cat('Zelda')
    zelda._hunger = 3
    stinky = Skunk('Stinky')
    keith = Unicorn('Keith')
    keith._hunger = 7
    lizzy = Dragon('Lizzy')
    lizzy._hunger = 1450 # 8)
    doggo = Dog('Doggo')
    doggo._hunger = 80
    kitty = Cat('Kitty')
    kitty._hunger = 80
    stinky_jr = Skunk('Stinky Jr.')  
    stinky_jr._hunger = 80
    clair = Unicorn('Clair')
    clair._hunger = 80
    mcfly = Dragon('McFly')
    mcfly._hunger = 80
    zoo_lst = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky, clair, mcfly]
    for animal in zoo_lst:
        print(type(animal), animal.get_name())
        while animal.is_hungry():
            animal.feed()# 5)
        animal.talk()    # 6)
        if isinstance(animal, Dog): 
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()    
    print('the zoo name is: {}'.format(animal.ZOO_NAME))        
    
    print('\n\n\n')
    print(type(Dog).__name__
        
if __name__ == '__main__':
    main()