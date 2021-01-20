import time

# Intro text
print("Your stomach starts to grumble.")
time.sleep(1.5)
print("You walk over to the freezer, open it and look in.")
time.sleep(1.5)
print("The freezer is empty, time to hunt!\n")
time.sleep(1.5)

# Data to be generated randomly
# Animals are {rabbit, deer, bull moose, black bear}
# wind direction is the direction it is coming from.
# distance is either close or far.
data = ["rabbit", "left", "close"]

# Player chooses weapon
print("You open the gun safe and see your pistol and rifle.")
time.sleep(1.5)
while True:
    choice = (input("Enter P to get the pistol\n"
                "Enter R to get the rifle\n").lower())
    if choice == "p":
        data.append("pistol")
        break
    if choice == "r":
        data.append("rifle")
        break

# Go hunting
print(f"You jump in your car and put the {data[3]} on the seat")
time.sleep(1.5)