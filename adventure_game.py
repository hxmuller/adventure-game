import time
import random

# Slow message printing for humans
# str - String to be printed
def print_slow(str):
    print(str)
    time.sleep(1.5)

# Print intro text
def intro_text():
    print_slow("\nYour stomach starts to grumble.")
    print_slow("You walk over to the freezer, open it and look in.")
    print_slow("The freezer is empty, time to hunt!\n")

# Player selects weapon
def select_weapon(data):
    choice = input("Enter P to get the pistol\n"
                   "Enter R to get the rifle\n"
                   "(Please enter P or R): ").lower()
    if choice == "p":
        data.append("pistol")
    elif choice == "r":
        data.append("rifle")
    else:
        select_weapon(data)

# Print travel text
def travel_text(data):
    print_slow(f"\nYou jump in your car and put the {data[3]} on the seat.")
    print_slow("Soon you are at the trail head and you park.")
    print_slow("You walk down the trail and come to a fork.")
    print_slow("The trail splits and goes hard left and hard right.")
    print_slow(f"You feel the wind on the {data[1]} side of your face.\n")

def select_trail(data):
    choice = input("Enter L to go left\n"
                   "Enter R to go right\n"
                   "(Please enter L or R): ").lower()
    if choice == "l":
        if data[1] == "left":
            data.append("against_wind")
            hunt(data)
        if data[1] == "right":
            data.append("with_wind")
            hunt(data)
    elif choice == "r":
        if data[1] == "left":
            data.append("with_wind")
            hunt(data)
        if data[1] == "right":
            data.append("against_wind")
            hunt(data)
    else:
        select_trail(data)

def hunt(data):
    print_slow("\nYou walk down the trail a bit and see a clearing.")
    print_range(data)
    print_slow(f"You raise your {data[3]}, carefully aim, and squeeze the trigger.")
    if data[2] == "close":
        if data[4] == "against_wind":
            print_slow(f"The {data[0]} drops to the ground. Success you have dinner!\n")
            select_again()
        elif data[4] == "with_wind":
            print_slow(f"The {data[0]} catches your scent, and runs away!\n")
            select_again()
    elif data[2] == "far":
        # Coin flip for pistol shot at a distance.
        if data[4] == "against_wind" and data[3] == "pistol":
            if random.randint(0,1) == 1:
                print_slow(f"The {data[0]} drops to the ground. Success you have dinner!\n")
                select_again()
            else:
                print_slow(f"The shot misses and startles the {data[0]}! It runs away.\n")
                select_again()
        elif data[4] == "against_wind" and data[3] != "pistol":
            print_slow(f"The {data[0]} drops to the ground. Success you have dinner!\n")
            select_again()
        elif data[4] == "with_wind":
            print_slow(f"The {data[0]} catches your scent, and runs away!\n")
            select_again()

def print_range(data):
    if data[2] == "close":
        prey_range = "a few"
    else:
        prey_range = "about 100"
    print_slow(f"As you approach the clearing, you see a {data[0]} {prey_range} meters away!")



def play_game():
    # Data to be generated randomly:
    #   data[0]: Animals are {'rabbit', 'deer', 'bull moose',
    #                         'black bear'}
    #   data[1]: Direction wind coming from is 'left' or 'right'
    #   data[2]: Distance to prey is 'close' or 'far'.
    # Data selected by player:
    #   data[3]: Weapon is 'pistol' or 'rifle'
    #   data[4]: Hunter to prey is 'against_wind' or 'with_wind'
    data = [random.choice(["rabbit", "deer", "bull moose", 
                           "black bear"]), 
            random.choice(["left", "right"]), 
            random.choice(["close", "far"])]
    intro_text()
    print_slow("You open the gun safe and see your pistol and rifle.")
    select_weapon(data)
    travel_text(data)
    print_slow("Which way will you go?")
    select_trail(data)

def select_again():
    choice = input("Would you like to play again? (y/n): ").lower()
    if choice == "y":
        play_game()
    elif choice == "n":
        print_slow("Thanks for playing!")
    else:
        select_again()

play_game()