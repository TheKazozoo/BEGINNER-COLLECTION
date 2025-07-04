class character:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.level = 0
        self.health = 100

    def introduction(self):
        print(f"Welcome {self.name}! You are a {self.job}, on level {self.level} with {self.health} health.")

    def level_up(self):
        self.level += 1
        print(f"You have leveled up! You are now level {self.level}.")

    def damage(self):
        self.health -= 2
        print(f"You took damage! Your health is now {self.health}.")

    def heal(self):
        self.health += 1
        print(f"You healed up! Your health is now {self.health}.")

print("Welcome to the academia!")
user_name = input("Please write your name: ")
user_job = input("Which job would you like to select? (Mage/Knight/Baker): ")

#user must write valid job
while user_job != "Mage" and user_job != "Knight" and user_job != "Baker":
    print("Error! Please pick valid job.")
    user_job = input("Which job would you like to select? (Mage/Knight/Baker): ")

user = character(user_name, user_job)

user.introduction()

input("Press enter to continue..")

print()
print("You encountered a mighty beast! It hits you hard.")
user.damage()

print()
choice1 = input("What do you do? (Heal/Do nothing): ")
if choice1 == "Heal":
    user.heal()
    user.level_up()
elif choice1 == "Do nothing":
    print("The poison resides inside you.")
    user.damage()
else:
    print("Invalid choice, you died! Game over")
    exit