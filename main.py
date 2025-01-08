import game_data


game_data.the_hero["name"] = input("What is your name, brave adventurer? > ")


# If the player decides to fight, this function will trigger
def fight():
    enemy_to_fight = game_data.enemies[0]
    in_fight = True  # Keeps us in the fight loop
    while in_fight:
        print(
            f"{game_data.the_hero['name']}, they have encountered the fearsome {enemy_to_fight['name']}"
        )
        battle_action = input("What would you like to do? > ")
        print("Fight has ended.")
        in_fight = False


# Boolean that will control the main game loop
game_on = True

while game_on:
    print(f"What would you like to do, {game_data.hero_name['name']}?")
    for option in game_data.main_options:
        print(f"{option['input_key']} {option['text']}")

    action = input(" > ")  # This will BLOCK the loop, until the user answers
    if action == "1":
        fight()
    elif action == "q":
        game_on = False
