import random

cmd = ""
spawned = False
spawned_mob_name = ''
spawned_mob_hp = 0
spawned_mob_xp = 0
player_health = 20
player_xp = 0
player_lvl = 0

weapons = {
    'old_sword': {
        'name': 'Old Sword',
        'min_dmg': 1,
        'max_dmg': 5
    }
}

mobs = {
    'boar': {
        'name': 'Boar',
        'health': 20,
        'xp': 10
    },
    'test': {
        'name': 'Test',
        'health': 99999
    }
}
while True:
    cmd = input("> ")
    cmd_arr = cmd.split()

    if 'help' in cmd:
        print("""
            help - Shows you a list of commands
            spawn - Spawns a mob of your choice
            mobs - Shows you a list of available mobs
            quit - Exits the game
        """)

    elif 'quit' in cmd:
        print("Thanks for playing :)")
        break

    elif 'mob' in cmd:
        for m_name in mobs:
            print(m_name)

    elif 'spawn' in cmd:
        if len(cmd_arr) == 2:
            try:
                mob = mobs.get(cmd_arr[-1])
                mob_name = mob['name']
                mob_hp = mob['health']
                mob_xp = mob['xp']
                if spawned:
                    print('Sorry, you can only spawn one mob at a time.')
                else:
                    if mob:
                        print(f'{mob_name} has been spawned with a health of {mob_hp}')
                        spawned_mob_name = f'{mob_name}'
                        spawned_mob_hp = mob_hp
                        spawned_mob_xp = mob_xp
                        spawned = True
            except TypeError:
                print("Sorry the mob doesn't exist. Type 'mobs' to see a list of available mobs.")
        else:
            print('Please choose a mob you want to spawn.')

    elif 'check' in cmd:
        if spawned:
            print(f"There is a {spawned_mob_name} in the area. Be careful! It's HP is {spawned_mob_hp}.")
        else:
            print('No mob has been spawned.')

    elif 'test' in cmd:
        mob = mobs.get(cmd_arr[-1])
        print(mob['name'])

    elif 'info' in cmd:
        print(f"""
            level - {player_lvl}
            xp - {player_xp}
            health - {player_health}
        """)

    elif 'attack' in cmd:
        if spawned:
            if spawned_mob_hp > 0:
                dmg = random.randint(1, 5)
                spawned_mob_hp -= dmg
                print(f"You've dealt {dmg} damage.")
                chance = [0, 0, 0, 1]
                chance = random.choice(chance)
                if chance == 1:
                    mob_dmg = random.randint(1, 3)
                    player_health -= mob_dmg
                    print(f"Boar has dealt {mob_dmg} damage to you!")
            else:
                print(f"You've successfully killed {spawned_mob_name}")
                print(f"+{spawned_mob_xp}")
                player_xp += spawned_mob_xp
                spawned = False
        else:
            print("You need to spawn a mob before attacking!")
    else:
        print("I don't recognize that command, please type 'help' to check the available commands.")