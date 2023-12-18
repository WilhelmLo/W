import random


def random_skada():
    return random.randint(1, 10) 



def hjälte_statistik():
    print("Din aktuella hälsa: ", player.hp)
    print("Din aktuella styrka: ", player.attack_power)

inventory = {}

def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")



    

class Monster:
    def __init__(self):
        self.name = random.choice(["skelett", "Zombie", "Apa", "mask"])
        self.hp = random.randint(1, 100)
        self.attack_power = random.randint(1, 100)

    def attack(self, player):
        player.hp -= self.attack_power
        print(f"{player.name} attackerar {self.name}!")
        print(f"{player.name}s aktuella hälsa: ", player.hp)

    def is_alive(self):
        return self.hp > 0

class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, monster):
        monster.hp -= self.attack_power
        print(f"{self.name} attackerar {monster.name}!")
        print(f"{monster.name}s aktuella hälsa: ", monster.hp)
    
    def increase_attack_power(self):
        self.attack_power += 5

    def increase_hp(self):
        self.hp += 5

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} gick in i en fälla tar skada: ", damage)
        print(f"{self.name}s aktuella hälsa: ", self.hp)
        
    def is_alive(self):
        return self.hp > 0
    



def chest(): 
    print("Du har hittat en kista!") 
    print("Vad vill du göra?") 
    print("1. Ta svärd") 
    print("2. Ta hjälm") 
    print("3. Gå vidare")
    val = input("Ange ditt val: ")

    if val == "1":
        print("Du har funnit ett svärd!")
        add_item("Svärd", 1)
        player.increase_attack_power()
    elif val == "2":
        print("Du har funnit en hjälm!")
        add_item("Hjälm", 1)
        player.increase_hp()
    elif val == "3":
        print("Du fortsätter.")
        return
    else:
       print("Välj 1, 2 eller 3!")
    chest()

player = Player("Hjälten", 30, 30)




def dörr_1():
    
    
    print("Du har hittat en stor dörr!")
    action = input("Vad vill du göra? (Gå in, Fly) ")
    if action.lower() == "gå in":
        dungeon_1()
    elif action.lower() == "fly":
        print("Du bestämmer dig för att fly.")
        return
    else:
        print("Du kan inte göra det. Prova igen.")
        dörr_1()

def dörr_2():
     
    print("Du har hittat en normal stor dörr!")
    action = input("Vad vill du göra? (Gå in, Fly) ")
    if action.lower() == "gå in":
        dungeon_2()
    elif action.lower() == "fly":
        print("Du bestämmer dig för att fly.")
        return
    else:
        print("Du kan inte göra det. Prova igen.")
        dörr_2()

def dörr_3():
   
    
    print("Du har hittat en liten dörr!")
    action = input("Vad vill du göra? (Gå in, Fly) ")
    if action.lower() == "gå in":
        dungeon_3()
    elif action.lower() == "fly":
        print("Du bestämmer dig för att fly.")
        return
    else:
        print("Du kan inte göra det. Prova igen.")
        dörr_3()

def dungeon_1():

    monster = Monster()

    print(f"Du har träffat på ett {monster.name}!")


    
    print(F"Du attackerar {monster.name}!")
    player.attack(monster)

    
    if not monster.is_alive():
        print(f"Du har besegrat {monster.name}!")
        player.increase_attack_power()
    else:
        print(f"{monster.name} attackerar dig!")
        monster.attack(player)

    return
    

       
    

def dungeon_2():
    player.take_damage(random_skada())

def dungeon_3():
    chest()

def dörr_val():
    val1 = random.randint(1,3)
    val = input("Vilken dörr vill du öppna? 1, 2, 3 eller 4:  ")
    if val == "1" or val == "2" or val == "3":
        if val1 == 1:
            dörr_1()
        elif val1 == 2:
            dörr_2()
        else:
            dörr_3()

    elif val == "4":
        return

    else:
        print("Välj 1, 2 eller 3!")
        dörr_val()




def main():


    print("Välkommen till mitt spel!")
 
    while player.hp >= 0:
    

        
    
   
      
        print(
            """

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            
            """)
        
        val = input("Ange ditt val: ")

        if val == "1":
            dörr_val()
        elif val == "2":
            view_inventory()
        elif val == "3":
            hjälte_statistik()
        else:
            print("Välj 1, 2 eller 3!")

main()