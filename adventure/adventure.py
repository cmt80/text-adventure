# setting up the inventory/hp for the start of the game
inventory = {
    "HP": 5,
    "Weapon": "fists",
    "Key": "none",
}

# creating inventory function
def check_inv():
    print("[ Inventory ]")
    print("# Current Health:", inventory["HP"])
    print("# Current Weapon:", inventory["Weapon"])
    print("# Current Key:", inventory["Key"])

# creating function to take player input for choices so i dont have to keep
# retyping it
def choose():
    currentChoice = input("> ")
    return currentChoice

# START OF ADVENTURE
print("You find yourself in a very dark dungeon.")
print("[1] Go left")
print("[2] Go right")

# call choice function
choice = choose()

# if player picks option one, start the GO LEFT path
if choice == "1":
    print("You decide to take the left corridor, venturing deeper into the dungeon.")
    print("Soon, you find a staff on the ground.")
    print("[1] Pick it up")
    print("[2] Leave it there")

    sec_choice = choose()
    if sec_choice == "1":
        print("You picked up the staff. [Staff added to inventory]")
        inventory["Weapon"] = "Staff"
    elif sec_choice == "2":
        print("You decide to leave the staff alone.")

    print("\nContinuing down the path, you encounter a strange creature that's unlike any\n" \
    " animal you've seen before. When it notices you, it starts growling like it wants to\n" \
    " attack you.")
    print("[1] Attack it first!")
    print("[2] Try to run past it")

    third_choice = choose()
    if third_choice == "1":
        # if player doesn't have a weapon, they cant kill the creature
        if inventory["Weapon"] == "fists":
            print("You lunge at the creature and start punching it,\n" \
            " showing NO mercy. But it has claws, sharp teeth, and is\n" \
            " otherwise unaffected by your weak little fists.")
            print("You get viciously attacked.")
            # subtract hp from player stats and display current hp
            inventory["HP"] -= 3
            print("-3 HP. You now have ", inventory["HP"], "HP left.")

            # attack again or try to escape
            print("[1] Attack it again")
            print("[2] Try to run past it")
            atk_choice = choose()

            # kill player and end game if they try to attack it again
            if atk_choice == "1":
                print("You try to attack the creature again, but its advantage over\n"
                " you is too great. You died.")
                quit()

            # allow player to escape but with reduced HP
            elif atk_choice == "2":
                print("You run past the creature. It doesn't follow you.")

        # if the player's weapon is the staff, they have a guaranteed chance to kill creature
        elif inventory["Weapon"] == "Staff":
            print("You wait for the creature to jump at you, then swiftly\n" \
            " attack it with your staff. After a few punishing whacks, the\n" \
            " creature dies.")

    # ignore combat and just continue down the left path
    elif third_choice == "2":
        print("With a running start, you jump over the creature and keep running\n" \
        " down the hall, not stopping until you're sure you lost it.")

    print("You continue deeper into the dungeon.")

# if the player picks option 2, start the GO RIGHT path
elif choice == "2":
    print("You decide to take the right corridor, venturing deeper into the dungeon.")
    print("Soon, you find a key on top of an old crate.")
    print("[1] Pick it up")
    print("[2] Leave it there")

    key_choice = choose()
    if key_choice == "1":
        print("You picked up the key. [Key added to inventory]")
        inventory.update({"Key": "yes"})