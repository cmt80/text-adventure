# setting up the inventory/hp for the start of the game
inventory = {
    "HP": 7,
    "Weapon": "fists",
    "Key": "no",
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
    # keeping it always active with while true
    while True:
        currentChoice = input("> ")

        # if 1 or 2 is entered, continue
        if currentChoice == "1" or currentChoice == "2":
            return currentChoice
        # if anything else is entered, show error message
        else:
            print("Invalid option. Enter 1 or 2")
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
    "animal you've seen before. When it notices you, it starts growling like it wants to\n" \
    "attack you.")
    print("[1] Attack it first!")
    print("[2] Try to run past it")

    third_choice = choose()
    if third_choice == "1":
        # if player doesn't have a weapon, they cant kill the creature
        if inventory["Weapon"] == "fists":
            print("You lunge at the creature and start punching it,\n" \
            "showing NO mercy. But it has claws, sharp teeth, and is\n" \
            "otherwise unaffected by your weak little fists.")
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
                "you is too great. You died.")
                quit()

            # allow player to escape but with reduced HP
            elif atk_choice == "2":
                print("You run past the creature. It doesn't follow you.")

        # if the player's weapon is the staff, they have a guaranteed chance to kill creature
        elif inventory["Weapon"] == "Staff":
            print("You wait for the creature to jump at you, then swiftly\n" \
            "attack it with your staff. After a few punishing whacks, the\n" \
            "creature dies.")

    # ignore combat and just continue down the left path
    elif third_choice == "2":
        print("With a running start, you jump over the creature and keep running\n" \
        "down the hall, not stopping until you're sure you lost it.")

    # continue the path
    print("\nYou continue deeper into the dungeon.")
    print("You soon come across a room with a number of pressure plates\n" \
    "covering the ground. It's impossible to get to the other side without\n" \
    "stepping on at least a few.")
    print("[1] Carefully traverse the pressure plates")
    print("[2] Jump and run to the other side as fast as possible")

    pres_choice = choose()
    if pres_choice == "1":
        # if you dont have the staff, you fail to pass through unharmed and lose 1 hp
        if inventory["Weapon"] == "fists":
            print("Even while being careful, your slowness made you get hit by an\n" \
            "arrow that had been activated and fired by one of the pressure plates\n" \
            "you stepped on.")
            print("You start quickly running to the other side after getting hit.")
            inventory["HP"] -= 1
            print("-1 HP. You now have ", inventory["HP"], "HP left.")

        # if you have the staff, you can pass through without losing any hp
        elif inventory["Weapon"] == "Staff":
            print("You use your staff to press every pressure plate in a straight\n" \
            "line, watching as a variety of arrows and spikes are summoned.\n" \
            "You then do the same thing, this time timing each trap in order to let you\n" \
            "pass through the room safely.")

    elif pres_choice == "2":
        print("You rush to the other side of the pressure plates as fast as\n" \
        "possible. Several arrows are fired and spikes are summoned, and you\n" \
        "almost get across without injury... until a mace falls on your head")
        print("You died.")
        quit()

    print("\nYou continue deeper into the dungeon..\n" \
    "The next room looks like a beautiful garden, something you\n" \
    "didn't expect to see in a dungeon like this.\n" \
    "\nYou approach a tree full of fruit.")

    print("[1] Take one of the fruits and eat it")
    print("[2] Ignore the fruits and continue to the next room")

    fruit_choice = choose()

    if fruit_choice == "1":
        print("You reach out and take a piece of fruit. It feels\n" \
        "nice and cool in the palm of your hand. You take a bite.")
        inventory["HP"] += 2
        print("After eating the fruit, you feel refreshed.")
        print("+2 HP. You now have ", inventory["HP"], "HP.")

    elif fruit_choice == "2":
        print("You ignore all of the trees, plants, and fruit.")

    print("\nYou continue through the dungeon.")

    print("While walking through the dark dungeon halls, something\n" \
    "shiny catches your eye.\n" \
    "A sword leaning against the wall.")

    print("[1] Take the sword")
    print("[2] Leave the sword there")

    sword_choice = choose()

    if sword_choice == "1":
        print("You pick up the sword. [Sword added to inventory]")
        inventory["Weapon"] = "Sword"

    elif sword_choice == "2":
        print("You decide to leave the sword there.")


    print("You continue through the dungeon.\n" \
    "Soon, you stumble across another aggressive creature.\n")

    print("\nYou have ", inventory["HP"], " HP.\n")

    print("[1] Attack the creature")
    print("[2] Try to evade it and flee")

    creature_choice = choose()

    if creature_choice == "1":
        # if the player has no weapons
        if inventory["Weapon"] == "fists":
            print("You try to punch the creature, but it attacks you first.")
            inventory["HP"] -= 1
            print("-1 HP. You have ", inventory["HP"], " HP left.")
            print("[1] Punch it again")
            print("[2] Flee")

            punch_choice = choose()

            if punch_choice == "1":
                print("You try to go for another punch, but\n" \
                "you just aren't strong enough. The creature\n" \
                "kills you.")
                print("You Lose.")
                quit()

            elif punch_choice == "2":
                print("You throw dirt at the creature as a\n" \
                "distraction before running past it into the next room.")


        elif inventory["Weapon"] == "Sword":
            print("You slice the creature with your sword, killing it quickly.")

        elif inventory["Weapon"] == "Staff":
            print("You hit the creature with your staff, but it grabs the\n"
            "staff with its mouth and yanks it out of your grasp.")
            
            print("[1] Flee")
            print("[2] Flee")
            inventory["Weapon"] = "fists"

            flee_choice = choose()

            if flee_choice == "1" or flee_choice == "2":
                print("With no other option left, you just run out of\n" \
                "the room. You leave your staff behind in exchange for\n" \
                "your life.")
                print("[Staff has been removed from inventory]")
            


    print("\n")
    # CHEST ENDING PATH
    print("You continue through the dungeon.")
    print("Soon, you reach something that is so amazing.\n" \
    "It's a golden chest, right in the center of the next room!!!!!\n" \
    "You can reach it by crossing a bridge")

    print("[1] Go open it immediately!!!!!")
    print("[2] Something's off...")

    chest_choice = choose()
    
    if chest_choice == "1":
        print("You run over to the chest and unlatch it, opening it and\n" \
        "revealing the contents to be......\n" \
        "a bunch of gold coins!")
        print("Shockingly, nothing bad even happens and now you're rich.")
        print("You Win.")
        quit()

    elif chest_choice == "2":
        # if the player doesnt have a weapon
        if inventory["Weapon"] == "fists" or inventory["Weapon"] == "Sword":
            print("Upon slightly closer inspection, you notice that the\n" \
            "chest is on a pedestal. There is a bridge that can allow you to\n" \
            "reach it, but approaching it from any other angle would cause you to\n" \
            "fall into a spiky moat surrounding the chest.")
            print("\nYou pick up a nearby rock and throw it at the chest.\n" \
            "Nothing happens.")

            print("[1] Throw a bigger rock.")
            print("[2] Cross the bridge and open the chest.")

            rock_choice = choose()
            if rock_choice == "1":
                print("You find an even bigger rock and throw it at the chest,\n" \
                "expecting to trigger some sort of trap.\n" \
                "Instead, the force of the rock causes the chest to topple off of\n" \
                "the pedestal, causing it to drop down into the deep, spiky moat below.\n" \
                "It explodes into a bunch of gold coins, now protected by the deadly spikes.")

                print("You failed to collect the treasure. You Lose.")
                quit()

            elif rock_choice == "2":
                print("You take the risk and walk across the bridge.\n" \
                "Surprisingly, there are no traps when you open the chest,\n" \
                "and it is filled to the brim with gold coins.")

                print("\nYou Win.")
                quit()
        
        elif inventory["Weapon"] == "Staff":
            print("Upon slightly closer inspection, you notice that the\n" \
            "chest is on a pedestal. There is a bridge that can allow you to\n" \
            "reach it, but approaching it from any other angle would cause you to\n" \
            "fall into a spiky moat surrounding the chest.")
            print("\nYou use the staff to poke the chest. Nothing happens.")
            print("[1] Poke it harder.")
            print("[2] Cross the bridge and open the chest.")

            poke_choice = choose()
            if poke_choice == "1":
                print("You poke the chest harder with the staff.\n" \
                "expecting to trigger some sort of trap.\n" \
                "Instead, the force of the poke causes the chest to topple off of\n" \
                "the pedestal, causing it to drop down into the deep, spiky moat below.\n" \
                "It explodes into a bunch of gold coins, now protected by the deadly spikes.")

                print("You failed to collect the treasure. You Lose.")
                quit()

            elif poke_choice == "2":
                print("You take the risk and walk across the bridge.\n" \
                "Surprisingly, there are no traps when you open the chest,\n" \
                "and it is filled to the brim with gold coins.")

                print("\nYou Win.")
                quit()
        


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

    elif key_choice =="2":
        print("You leave the key there.")

    print ("You continue through the dungeon, and soon you reach a door.")

    print("[1] Open the door")
    print("[2] Go back and exit dungeon")

    door_choice = choose()
    if door_choice == "1":
        if inventory["Key"] == "yes":
            print("You use the key to unlock the door, then proceed.")
        elif inventory["Key"] == "no":
            print("The door is locked. You can't open it.\n" \
            "You Lose.")
            quit()

    elif door_choice == "2":
        print("You decide to just give up and leave the dungeon.")
        quit()

   

    print("\nOn the other side of the door is something that is so amazing.\n" \
    "It's a golden chest, right in the center of the next room!!!!!")

    print("[1] Go open it immediately!!!!!")
    print("[2] Something's off...leave the dungeon")

    ch_choice = choose()
    
    if ch_choice == "1":
        print("You run over to the chest and unlatch it, opening it and\n" \
        "revealing the contents to be......\n" \
        "a bunch of gold coins!")
        print("Shockingly, nothing bad even happens and now you're rich.")
        print("You Win.")
        quit()

    elif ch_choice == "2":
        print("You have a bad feeling about the chest,\n" \
        "and you didn't even want treasure that bad anyway.")

        print("\nYou ignore the chest and exit the dungeon.")
        quit()