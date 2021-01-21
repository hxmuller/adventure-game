import time

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
    if choice == "r":
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
        if data[1] == "right":
            data.append("with_wind")
    if choice == "r":
        if data[1] == "left":
            data.append("with_wind")
        if data[1] == "right":
            data.append("against_wind")
    else:
        select_trail(data)

# Data to be generated randomly
# Animals are {rabbit, deer, bull moose, black bear}
# wind direction is either from left or right
# distance is either close or far.
data = ["rabbit", "left", "close"]
intro_text()
print_slow("You open the gun safe and see your pistol and rifle.")
select_weapon(data)
travel_text(data)
print_slow("Which way will you go?")
select_trail(data)
