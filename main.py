from battle_engine import battle_engine
import game_data


game_data.the_hero["name"] = input("What is your name, brave adventurer? > ")

# Boolean that will control the main game loop
game_on = True
while game_on:
    print(f"What would you like to do, {game_data.hero_name['name']}?")
    for option in game_data.main_options:
        print(f"{option['input_key']} {option['text']}")

    action = input(" > ")  # This will BLOCK the loop, until the user answers
    if action == "1":
        battle_engine()
    elif action == "q":
        game_on = False
