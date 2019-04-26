import random

class Alive:
    def __init__(self, hp):
        self.hp = hp

    def hp_lower(self, hpdown):
        self.hp -= hpdown
    
class Survivors(Alive):
    def attack(self):
        a=random.randint(0,20)
        print(f'Выживший: "Дыжь!". Минус {a} очков у зомби')
        Z.hp_lower(a)
    
class Zombies(Alive):
    def attack(self):
        a=random.randint(0,20)
        print(f'Зомби: "Хрусь!". Минус {a} очков у Выжившего')
        S.hp_lower(a)

S = Survivors(hp=100)
Z = Zombies(hp=100)

for _ in range(100):
    S.attack()
    if Z.hp <=0:
        print('Выживший: "И так будет с каждым"')
        break
    Z.attack()
    if S.hp <=0:
        print('Зомби: "ЫЫЫЫыыЫыЫы"')
        break
