import random
import time
import Combat_screen as combatscreen
class Action:
    def __init__(self, name, damage_modifier=1, action_time=1):
        self.name = name
        self.damage_modifier = damage_modifier
        self.action_time = action_time
        self.start_time = 0
        self.finish_time = 0

    def start(self, current_time):
        self.start_time = current_time
        self.finish_time = current_time + self.action_time

    def is_active(self, current_time):
        return self.start_time <= current_time < self.finish_time

    def apply(self, source, target):
        damage = random.randint(1, 10) * self.damage_modifier
        target.health -= damage
        print(f"{source.name} uses {self.name} on {target.name} for {damage} damage!")



class Unit():
    def __init__(self, name, maxhealth, damage, attacktime, sounds = "Default", owner = "computer",
                 target = 0, action = "attack", action_start = 0, isalive = True, xp = 0, xptolv = 100, level = 1, actions = []):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.damage = damage
        self.attacktime = attacktime
        self.sounds = sounds
        self.owner = owner
        self.target = target
        self.action = action
        self.action_start = action_start
        self.action_end = self.action_start + self.attacktime
        self.isalive = isalive
        self.xp = xp
        self.xptolv = xptolv
        self.level = level
        if(self.owner == "computer"):
            self.xp = self.maxhealth * self.damage * 100 /self.attacktime
        self.actions = actions
    def clone(self):
        # Create a new instance with the same initial attributes
        return Unit(
            self.name,
            self.maxhealth,
            self.maxhealth,  # Set initial health to maxhealth
            self.damage,
            self.attacktime,
            self.sounds,
            self.owner,
            self.target,
            self.action,
            self.action_start,
            self.isalive,
            self.xp,
            self.xptolv,
            self.level,
            self.actions)

    def perform_action(self, target, current_time):
        if not hasattr(self, 'current_action') or not self.current_action.is_active(current_time):
            self.current_action = random.choice(self.actions)
            self.current_action.start(current_time)

        if self.current_action.is_active(current_time):
            self.current_action.apply(self, target)
            combatscreen.update_action_display(
                0 if self.name == rat.name else 1,
                current_time,
                self.current_action.start_time,
                self.current_action.finish_time
            )



# Define actions
bite_action = Action("Bite", damage_modifier=2, action_time=100)
scratch_action = Action("Scratch", damage_modifier=1, action_time=200)

# Create units
rat = Unit("Rat", 200, 10, 1, actions=[bite_action], owner = "player")
dog = Unit("Dog", 440, 9, 2, actions=[bite_action, scratch_action])

# Simulate the fight
combatscreen.generate_combat_window([rat, dog])

def game_time():
    pause = combatscreen.checkpause()
    if not pause:
        combattime()
    combatscreen.combat.after(1000, game_time)  # Schedule the next check

def combattime():
    global turn
    if rat.health > 0 and dog.health > 0:
        rat.perform_action(dog, turn)
        dog.perform_action(rat, turn)
        update_combat_screen()
        turn += 1
    else:
        display_final_result()

def update_combat_screen():
    combatscreen.update_health_display(0, rat.health, rat.maxhealth)
    combatscreen.update_health_display(1, dog.health, dog.maxhealth)
    combatscreen.update_action_display(0, turn, rat.current_action.start_time, rat.current_action.finish_time)
    combatscreen.update_action_display(1, turn, dog.current_action.start_time, dog.current_action.finish_time)
    # Add other necessary updates (like update_action_display)

def display_final_result():
    print("\nFinal Result:")
    print(f"{rat.name}'s health: {rat.health}")
    print(f"{dog.name}'s health: {dog.health}")
    if rat.health <= 0:
        print(f"{rat.name} has been defeated!")
    elif dog.health <= 0:
        print(f"{dog.name} has been defeated!")
    else:
        print("It's a draw!")

turn = 0
game_time()  # Start the game time loop
combatscreen.start_combat()  # Start the combat GUI