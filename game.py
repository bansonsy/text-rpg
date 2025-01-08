hero_name = input("What is your name, brave adventurer? > ")


the_hero = {
    "name": hero_name,
    "xp": 0,  # Use XP to determine when to level up
    "level": 1,
    "gold": 5,  # Amount of money the player has
    "attack_power": 5,
    "defense": 2,
    "hp": 10,
    "weapon": "fists",
    "inventory": [
        "health_potion",
    ],
}


enemies = []
zombie = {
    "name": "Zombie",
    "hp": 10,
    "attack_power": 3,
    "defense": 0,
    "weapon": "fist",
    "xp_drop": 2,
    "gold_drop": 1,
    "power": {
        "name": "Berzerk",
        "effect": "attack_up",
        "effect_impact": 5,
    },
}


enemies.append(zombie)


main_options = [
    {"text": "Fight a monster.", "input_key": "1"},
    {"text": "Go to the shop.", "input_key": "2"},
    {"text": "Do a dance.", "input_key": "3"},
    {"text": "Sleep and adventure another day. (EXIT GAME)", "input_key": "q"},
]


# If the player decides to fight, this function will trigger
def fight():
    enemy_to_fight = enemies[0]
    in_fight = True  # Keeps us in the fight loop
    while in_fight:
        print(
            f"{the_hero['name']}, they have encountered the fearsome {enemy_to_fight['name']}"
        )
        battle_action = input("What would you like to do? > ")
        print("Fight has ended.")
        in_fight = False


# Boolean that will control the main game loop
game_on = True

while game_on:
    print(f"What would you like to do, {hero_name['name']}?")
    for option in main_options:
        print(f"{option['input_key']} {option['text']}")

    action = input(" > ")  # This will BLOCK the loop, until the user answers
    if action == "1":
        fight()
    elif action == "q":
        game_on = False
