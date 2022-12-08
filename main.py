# THIS IS A PRE-RELEASE VERSION. BUILD 3

# Import necessary modules
import random
import pickle

# Define a class to represent the user
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100 # Starting health
        self.money = 0 # Starting money
        self.items = [] # Starting items
        
    # Method to simulate the passage of time
    def time_passes(self):
        self.age += 1 # Increase the user's age by 1
        
        # Randomly generate an event for the user based on their age
        if self.age <= 5:
            # Young child events
            events = ["goes to school", "plays with friends", "learns to read"]
            print(self.name + " " + random.choice(events))
        elif self.age <= 18:
            # Teenager events
            events = ["goes to high school", "gets a part-time job", "gets their driver's license"]
            print(self.name + " " + random.choice(events))
        else:
            # Adult events
            events = ["starts a career", "gets married", "has a child"]
            print(self.name + " " + random.choice(events))
            
        # Randomly generate a financial event for the user
        if random.random() < 0.5:
            # 50% chance of earning money
            self.money += random.randint(100, 500)
            print(self.name + " earns $" + str(self.money) + ".")
        else:
            # 50% chance of losing money
            self.money -= random.randint(100, 500)
            if self.money < 0:
                self.money = 0
            print(self.name + " loses $" + str(self.money) + ".")
            
    # Method to simulate illness and injury
    def get_sick(self):
        self.health -= random.randint(10, 30) # Decrease health by a random amount
        
        # Check if the user's health is below 0, indicating death
        if self.health <= 0:
            print(self.name + " has died.")
        else:
            print(self.name + " is feeling sick and their health has decreased.")
        
    # Method to simulate visiting a doctor
    def visit_doctor(self):
        # Check if the user has enough money to pay for a doctor's visit
        if self.money >= 50:
            self.money -= 50 # Pay for the doctor's visit
            self.health += 20 # Increase the user's health
            
            # Check if the user's health is above 100, indicating full recovery
            if self.health > 100:
                self.health = 100 # Set the user's health to 100
                print(self.name + " is now fully recovered.")
            else:
                print(self.name + " visits a doctor and their health improves.")
    
    # Method to simulate shopping
    def shop(self):
    # Generate a list of items for the user to choose from
    items = ["food", "clothes", "toys", "books"]
    
    # Print the available items and their prices
    print("Available items:")
    for item in items:
        print("- " + item + ": $" + str(random.randint(10, 100)))
        
    # Prompt the user to make a selection
    print("Enter the name of the item you would like to purchase:")
    selection = input()
    
    # Check if the user entered a valid item
    if selection in items:
        # Check if the user has enough money to purchase the item
        item_price = random.randint(10, 100)
        if self.money >= item_price:
            # Add the item to the user's list of items
            self.items.append(selection)
            self.money -= item_price # Deduct the cost of the item from the user's money
            print(self.name + " purchases a " + selection + " for $" + str(item_price) + ".")
        else:
            print(self.name + " does not have enough money to purchase a " + selection + ".")
    else:
        print(self.name + " did not enter a valid item.")

# Method to save the user's data
def save_data(self):
    # Serialize the user's data using pickle
    data = pickle.dumps(self)
    
    # Write the serialized data to a file
    with open("user_data.pkl", "wb") as f:
        f.write(data)

# Method to restore the user's data
def restore_data(self):
    # Read the serialized data from the file
    with open("user_data.pkl", "rb") as f:
        data = f.read()
    
    # Deserialize the data using pickle
    self = pickle.loads(data)
