the_hero = {
    "name": "Incognito",
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


goblin = {
    "name": "Goblin",
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
