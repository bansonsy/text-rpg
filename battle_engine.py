import game_data
import random


# If the player decides to fight, this function will trigger
def fight():
    total_enemies = len(game_data.enemies)
    random_index = random.randint(0, total_enemies - 1)
    enemy_to_fight = game_data.enemies[random_index].copy()

    in_fight = True  # Keeps us in the fight loop
    print(
        f"{game_data.the_hero['name']}, they have encountered the {enemy_to_fight['adjective']} {enemy_to_fight['name']}"
    )
    while in_fight:
        enemy_attack_modifier = 1

        print(
            f"You have {game_data.the_hero['hp']} health points. Your enemy has {enemy_to_fight['hp']} health points."
        )
        print(f"1. Attack with the {game_data.the_hero['weapon']}")

        health_potion_count = game_data.the_hero["inventory"].count("health_potion")
        print(f"2. Drink the health potion. You have {health_potion_count} potions.")
        print("3. Defend and heal.")
        print("4. Do a little dance.")
        print("5. Run for your life.")

        # Hero's Turn
        battle_action = input("What would you like to do? > ")
        if battle_action == "1":
            # Take the hero's attack power - monster's defense
            # Reduce monster's hp by hero_power_hit
            hero_power_hit = (
                game_data.the_hero["attack_power"] - enemy_to_fight["defense"]
            )
            enemy_to_fight["health"] -= hero_power_hit

            print(
                f"You have struck the with {game_data.the_hero['weapon']} for {hero_power_hit} damage."
            )

        elif battle_action == "2":
            if health_potion_count > 0:
                # Restore all HP
                game_data.the_hero["inventory"].remove("health_potion")
                game_data.the_hero["hp"] = game_data.the_hero["max_hp"]
                print("You have restored to full health.")
            else:
                # No potions
                print("You got no potions.")
                enemy_attack_modifier = 2

        elif battle_action == "5":
            print("Fight has ended.")
            in_fight = False

        # Enemy's turn, if alive
        if enemy_to_fight["hp"]:
            # Attack back
            monster_power_hit = (
                enemy_to_fight["attack_power"] * enemy_attack_modifier
            ) - game_data.the_hero["defense"]
            print(
                f"The enemy {enemy_to_fight['name']} has struck you with {enemy_to_fight['weapon']} for {monster_power_hit} damage."
            )
            game_data.the_hero["hp"] -= monster_power_hit
        else:
            print(
                f"Congratulations {game_data.the_hero['name']}. You have slain the {enemy_to_fight}"
            )
            # Grant some gold and xp
            game_data.the_hero["gold"] += enemy_to_fight["gold_drop"]
            game_data.the_hero["xp"] += enemy_to_fight["xp_drop"]
            print(
                f"You have gained {enemy_to_fight['gold_drop']} gold and {enemy_to_fight['xp_drop']} xp points."
            )
            print(
                f"You now have {game_data.the_hero['gold']} gold and {game_data.the_hero['xp']} xp."
            )
            in_fight = False
