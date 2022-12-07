# THIS IS A PRE-RELEASE BUILD. Build 218.

import random
import os


class Character:

  def __init__(self):
    self.age = 0
    self.health = 100
    self.wealth = 100
    self.food_and_water_count = 0
    self.exercise_count = 0
    self.actions_count = 0
    self.age_description = "Newborn - 0-12 months"
    self.prev_age_description = "Newborn - 0-12 months"
    self.real_age = 0

  def eat(self):
    self.health = min(100, self.health + 10)
    self.food_and_water_count += 1
    self.actions_count += 1
    self.check_age_up()
    return self

  def drink(self):
    self.health = min(100, self.health + 5)
    self.food_and_water_count += 1
    self.actions_count += 1
    self.check_age_up()
    return self

  def exercise(self):
    self.health = min(100, self.health + 5)
    self.food_and_water_count += 1
    self.actions_count += 1
    self.check_age_up()
    return self

  def age_up(self):
    self.prev_age_description = self.age_description
    self.age += 1
    self.health = 0 if self.food_and_water_count == 0 else max(
      0, self.health - 50) if self.food_and_water_count < 3 else self.health

    self.real_age = self.age

    if self.age == 0:
      self.age_description = "Newborn - 0-12 months"
    elif self.age >= 1:
      self.age_description = "Child - 1-13 years"
    elif self.age >= 13 and self.age <= 24:
      self.age_description = "Adolescent - 14-24 years"
    elif self.age >= 25 and self.age <= 64:
      self.age_description = "Adult - 25-65 years"
    elif self.age >= 65:
      self.age_description = "Elderly - 65+ years"

    return self

  def check_age_up(self):
    if self.actions_count % 5 == 0:
      self.age_up()
    return self

  def get_death_probability(self):
    return 0.96**(self.age / 100)

  def check_death(self):
    if self.get_death_probability() > random.uniform(0, 1):
      self.health = 0
    return self


class Game:

  def __init__(self):
    self.character = Character()

  def process_command(self, command):
    if command == "eat":
      self.character.eat()
    elif command == "drink":
      self.character.drink()
    elif command == "exercise":
      self.character.exercise()
    elif command == "age_up":
      self.character.age_up()
    else:
      print("Invalid command.")


game = Game()

while True:
  if game.character.health <= 0:
    os.system("clear")
    print("You have died.")

    response = input("Would you like to restart? (y/n)")
    if response.lower() == "y":
      game = Game()
    else:
      break

  command = input("Enter a command: ")
  game.process_command(command)

  print(f"Age: {game.character.age_description}")
  print(f"Real Age: {game.character.real_age}")
  print(f"Previous Age: {game.character.prev_age_description}")
  print(f"Health: {game.character.health}")
  print(f"Wealth: {game.character.wealth}")
