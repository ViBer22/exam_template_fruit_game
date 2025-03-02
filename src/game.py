from .grid import Grid
from .player import Player
from . import pickups
from .enemy import Enemy
import random

player = Player(18, 6)
score = 0
inventory = []
grace_steps = 0
move_counter = 0
bomb = None
collected_chests =0
enemies = [Enemy(5,5), Enemy (30,2)]

g = Grid()
g.set_player(player)
g.make_walls()

initial_items = pickups.randomize(g, num_keys=1)  #placera alla föremål


def print_status():
    print(f"\nPoäng: {score} | Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    print(g.__str__(enemies=enemies))

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status()
    move_counter +=1

    # Hantera automatiskt genererade händelser
    if move_counter % 25 == 0:
        x, y = g.get_random_x(), g.get_random_y()
        if g.is_empty(x, y):
            fruit = random.choice([i for i in pickups.pickups if i.value == 20])
            g.set(x, y, fruit)
            print("Ny frukt växer fram!")
    # Fiender rör sig varje drag
        for e in enemies:
            e.move_towards(player.pos_x, player.pos_y, g)
            if e.pos_x == player.pos_x and e.pos_y == player.pos_y:
                score -= 20
                print("Fiende fångade dig! -20 poäng")

    command = input("Use WASD to move, Q/X to quit. ").casefold()[:2]  # Tillåt 2 tecken

    if command[0] in ["q", "x"]:
        break

        # Hantera kommandon
    if command.startswith("j") and len(command) == 2:  # Hopp-kommando
        dir = command[1]
        dx, dy = 0, 0
        if dir == "w":
            dy = -2
        elif dir == "s":
            dy = 2
        elif dir == "a":
            dx = -2
        elif dir == "d":
            dx = 2
        # Hopphantering med väggkollision
        for _ in range(2):
            if player.can_move(dx // 2, dy // 2, g):
                player.move(dx // 2, dy // 2)
                if grace_steps <= 0: score -= 1
            else:
                break

    elif command == "b":  # Bomb-kommando
        bomb = (player.pos_x, player.pos_y, 3)
        print("Bomb placerad!")

    elif command == "t":  # Desarmera fälla
        cell = g.get(player.pos_x, player.pos_y)
        if isinstance(cell, pickups.Trap):
            g.clear(player.pos_x, player.pos_y)
            print("Fälla desarmerad!")

    elif command[0] in ["w", "a", "s", "d"]:  # Vanlig rörelse
        dx, dy = 0, 0
        if command[0] == "w":
            dy = -1
        elif command[0] == "s":
            dy = 1
        elif command[0] == "a":
            dx = -1
        elif command[0] == "d":
            dx = 1

        if player.can_move(dx, dy, g):
            player.move(dx, dy)
            # The floor is lava med grace period
            if grace_steps <= 0:
                score -= 1
            else:
                grace_steps -= 1

            # Hantera plockande av föremål
            cell = g.get(player.pos_x, player.pos_y)
            if isinstance(cell, pickups.Item):
                if isinstance(cell, pickups.Trap):
                    score += cell.value
                elif isinstance(cell, pickups.Chest):
                    if "key" in inventory:
                        score += cell.value
                        inventory.remove("key")
                        collected_chests += 1
                        g.clear(player.pos_x, player.pos_y)
                    else:
                        print("Saknar nyckel!")
                else:
                    score += cell.value
                    inventory.append(cell.name)
                    grace_steps = 5
                    g.clear(player.pos_x, player.pos_y)

        # Hantera bombexplosion
    if bomb:
        bx, by, timer = bomb
        timer -= 1
        if timer <= 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    g.set(bx + dx, by + dy, g.empty)
            bomb = None
            print("Bomben exploderade!")
        else:
            bomb = (bx, by, timer)

        # Kolla vinstvillkor
    if (len(inventory) + collected_chests) >= initial_items:
        if g.get(35, 11) != "E":
            g.set(35, 11, "E")
            print("Utgång öppen!")
        elif player.pos_x == 35 and player.pos_y == 11:
            print("GRATTIS! Du vann!")
            break


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")