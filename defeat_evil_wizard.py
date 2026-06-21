import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.block_next_attack = False      # Flag to indicate if the character will block the next attack

# Attack() method that calculates damage based on attack power and reduces opponent's health.
    def attack(self, opponent):
        # Check if opponent blocks the attack
        if opponent.block_next_attack:
            print(f"{opponent.name} blocks/dodges the attack!")
            opponent.block_next_attack = False
            return
        # Randomize the damage of the attack within a range.    
        damage = random.randint( max(1, self.attack_power - 5), self.attack_power + 5 )
        opponent.health = max(0, opponent.health - damage)

        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        print( f"{opponent.name} has " f"{opponent.health}/{opponent.max_health} health remaining." )

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # Implement a heal() method that restores health but does not exceed the maximum.
    # Randomize the ability to heal within a range 
    def heal(self):
        heal_amount = random.randint(1,10)
        old_health = self.health
        self.health = min(self.max_health, self.health + heal_amount)
        healed = self.health - old_health
        print(f"{self.name} heals for {healed} points! Current health: {self.health}/{self.max_health}")

    # Display the character's stats, including health and attack power.
    def display_stats(self):
        print(f"\n---- Character Stats ---")
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
# Warrior : A kickboxer pro with the abilities of fast kicking moves and dodges the kicks.
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def kick(self, opponent):
        if opponent.block_next_attack:
            print(f"{opponent.name} blocks/dodges the kick!")
            opponent.block_next_attack = False
            return
        
        damage = random.randint( self.attack_power + 5, self.attack_power + 10 )
        opponent.health = max(0, opponent.health - damage)
        print( f"\n{self.name} performs a powerful kick on " f"{opponent.name} for {damage} damage!" )
        print( f"{opponent.name} has " f"{opponent.health}/{opponent.max_health} health remaining." )
        
    def dodge(self):
        self.block_next_attack = True
        print(f"\n{self.name} prepares to dodge the next attack!")


# Mage class (inherits from Character)
# Mage : A dragon slayer with the abilities of spurring fireballs and disappearing in the smoke.
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    # Randomize the damage of the fireball attack within a range.
    def fireball(self, opponent):
        if opponent.block_next_attack:
            print(f"{opponent.name} blocks/dodges the fireball!")
            opponent.block_next_attack = False
            return
        
        damage = random.randint( self.attack_power + 5, self.attack_power + 10 )
        opponent.health = max(0, opponent.health - damage)
        print( f"\n{self.name} spurs a fireball at " f"{opponent.name} for {damage} damage!" )
        print( f"{opponent.name} has " f"{opponent.health}/{opponent.max_health} health remaining." )
        
    def disappear(self):
        self.block_next_attack = True
        print(f"{self.name} disappears in the smoke!")


# Create Archer class (inherits from Character)
# Archer: A ranged attacker with abilities to shoot arrows and evade attacks.
# Archer: "Quick Shot" (double arrow attack) and "Evade" (evades the next attack ).

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    # Randomize the damage of the quick shot attack within a range.
    def quick_shot(self, opponent):
        if opponent.block_next_attack:
            print(f"{opponent.name} blocks/dodges the arrows!")
            opponent.block_next_attack = False
            return
        
        damage1 = random.randint(max(1, self.attack_power - 5), self.attack_power + 5)
        damage2 = random.randint(max(1, self.attack_power - 5), self.attack_power + 5)
        total_damage = damage1 + damage2
        opponent.health = max(0, opponent.health - total_damage)
        print(f"\n{self.name} strikes a double arrow attack at {opponent.name} for {total_damage} damage!")
        print(f"{opponent.name} has {opponent.health}/{opponent.max_health} health remaining.")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.block_next_attack = True
        print(f"{self.name} evades the next attack!")

# Create Paladin class
# Paladin: A defensive hero who can heal and shield against attacks.
# Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=15)

    # Randomize the damage of the holy strike attack within a range.
    def holy_strike(self, opponent):
        if opponent.block_next_attack:
            print(f"{opponent.name} blocks the Holy Strike!")
            opponent.block_next_attack = False 
            return
            
        damage = random.randint( self.attack_power * 2 - 5, self.attack_power * 2 + 5 )
        opponent.health = max(0, opponent.health - damage)
        print( f"\n{self.name} performs a Holy Strike on " f"{opponent.name} for {damage} damage!" )
        print( f"{opponent.name} has " f"{opponent.health}/{opponent.max_health} health remaining." )
            
    def divine_shield(self):
        self.block_next_attack = True
        print( f"{self.name} activates Divine Shield " f"and will block the next attack!" )
    

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def dark_blast(self, opponent):
        damage = random.randint(30, 50)
        opponent.health = max(0, opponent.health - damage)
        print( f"\n{self.name} casts a dark blast on " f"{opponent.name} for {damage} damage!" )
        print( f"{opponent.name} has " f"{opponent.health}/{opponent.max_health} health remaining." )

    def regenerate(self):
        self.health = min(self.max_health, self.health + 5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")
 

# Create a turn-based battle system where the player and the evil wizard take turns
# attacking each other until one of them is defeated. The player can choose to attack,
# use a special ability, or heal during their turn. The evil wizard will attack the player after each turn.
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    quit_game = False

    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Defensive Ability")
        print("4. Heal")
        print("5. View Stats")
        print("6. Quit Game")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)

        elif choice == "2":                            
            if isinstance(player, Warrior):      #check the type of player and call the appropriate special ability method
                player.kick(wizard)
            elif isinstance(player, Mage):
                player.fireball(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)

        elif choice == "3":                            
            if isinstance(player, Warrior):      #check the type of player and call the appropriate special ability method
                player.dodge()
            elif isinstance(player, Mage):
                player.disappear()
            elif isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()

        elif choice == "4":
            player.heal()                       # Call the heal method to restore health

        elif choice == "5":
            player.display_stats()
            continue                # Skip the wizard's turn to allow the player to view stats without taking damage
       
        elif choice == "6":
            quit_game = True
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

# Evil wizard regenerates health and attacks the player after each turn
        if wizard.health > 0:
            print("\n--- Evil Wizard's Turn ---")
        if wizard.health > 0:
            wizard.regenerate()
            if random.random() < 0.25:                 # Less than 25% chance of a special attack
                wizard.dark_blast(player)
            else:
                wizard.attack(player)
  

        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    if quit_game:
        return

    if wizard.health <= 0:
        print(f"Congratulations, {player.name} is the winner!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    print("\nA powerful enemy approaches!")
    battle(player, wizard)

if __name__ == "__main__":
    main()