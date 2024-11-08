class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def attack(self, target):
        print(f"атакує !")


    def take_damage(self,damage):
        self.health -= damage
        print(f"отримав {damage} ушкоджень. Поточне здоров'я")


    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon


    def attack(self, target):
        damage = 10
        if self.weapon == "меч":
            damage += 5
        elif self.weapon == "лук":
            damage += 3
        print(f"атакує за допомогою")
        target.take_damage(damage)

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


    def attack(self, target):
        print(f"атакує і завдає ушкоджень!")
        target.take_damage


hero = Hero("Герой", 100, "меч")
enemy = Enemy("Ворог", 80, 15)


hero.attack(enemy)


enemy.attack(hero)


if hero.is_alive():
    print(f"ще живий!")
else:
    print(f"мертвий!")

if enemy.is_alive():
    print(f"ще живий!")
else:
    print(f"мертвий!")
