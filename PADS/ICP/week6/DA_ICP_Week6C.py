import random

class Character:

    def __init__(self, name, hp, atk, defense) -> None:
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__defense = defense

    def attack(self, target):

        """
        Handles attacks between characters
        
        Calculates damage based on based on attacker's attack power and target's defense
        
        If target's hp<=0: indicates defeat
        
        """

        damage = max(0, self.__atk, target.__defense)
        target.__hp -= damage
        
        print(f"{self.__name} attacks {target.__name} for {damage} damage!\n")

        if target.__hp <=0:
            print(f"{target.__name} has been defeated!\n")

    def show_status(self):

        """
        Displays status of character.
        """

        print(f"{self.__name}\n HP: {self.__hp}\n ATK: {self.__atk}\n Defense: {self.__defense}")

    def special_move(self, target):
        pass

class Hero(Character):
    
    def __init__(self, name, hp, atk, defense, role) -> None:
        super().__init__(name, hp, atk, defense)
        self.__role = role

    def special_move(self, target: Character):

        """
        Overrides the parent class abstact method. 
        
        Provies special move based on hero's role
        """
        
        if self.__role == "Healer":

            heal = random.randint(50, 60)
            target.__hp+=heal
            print(f"{self.__name} uses Healing, restoring {heal} HP to {target.__name}!\n")

        if self.__role == "Warrior":
            
            print(f"{self.__name} uses Valor, and deals triple damage!\n")
            damage = max(0, self.__atk*3 - target.__defense)
            target.__hp-=damage

            print(f"{self.name} attacks {target.__name} for {damage} damage!\n")

            if target.__hp <=0:
                print(f"{target.__name} has been defeated!\n")

class Monster(Character):

    def __init__(self, name, hp, atk, defense, role="") -> None:
        super().__init__(name, hp, atk, defense)
        self.__role = role

    def special_move(self, target: Character):

        """
        Overrides parent's abstract method
        Reduces target attack's power by half if monster's role is Boss
        """
        
        if self.__role == "Boss":
            target.__atk = target.__atk / 2

def main():
    pass
        

    