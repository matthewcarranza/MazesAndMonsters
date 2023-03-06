# Matt Carranza
# Due Date: 11/10/2022
# Assignment Summary: A game that allows the user to wander through a dungeon maze and fight monsters that they encounter as they explore.

import hero
import beginner_factory
import expert_factory
import map
from check_input import get_int_range 
from random import randint

def main():
  name = input("What is your name, traveler? ")
  h = hero.Hero(name, 25)
  m = map.Map()
  
  difficulty = get_int_range("Difficulty:\n1. Beginner\n2. Expert\n", 1, 2)
  if difficulty == 1:
    factory = beginner_factory.BeginnerFactory()
  if difficulty == 2:
    factory = expert_factory.ExpertFactory()

  counter = 1
  choice = 0
  while (h.hp != 0 and choice != 5):
    print(h)
    m.reveal(h.loc)
    print(m.show_map(h.loc))
    
    dir = '*'
    choice = get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter Choice: ", 1, 5)
    
    if choice != 5:
      if choice == 1:
        dir = h.go_north()
      elif choice == 2:
        dir = h.go_south()
      elif choice == 3:
        dir = h.go_east()
      elif choice == 4:
        dir = h.go_west()
      if dir == 'x': #If the hero runs away and lands on another monster and moves toward off the map but remains on that same monster, should it still run?
        print("You cannot go that way...")
      
      #If there is nothing there:
      if dir == 'n':
        print("There is nothing here...")

      #If landing back on start:
      if dir == 's':
        print("You found yourself back at the starting place.")
      
      #Monster Battle
      if dir == 'm':
        e = factory.create_random_enemy()
        print("You encountered a ", end="")
        print(e)
        atk_menu = 0
        while e.hp != 0 and h.hp != 0 and atk_menu != 2:
          atk_menu = get_int_range("1. Attack " + e.name + "\n2. Run Away\nEnter Choice: ", 1, 2)
          if atk_menu == 1:
            print(h.attack(e))
            if e.hp != 0:
              print(e.attack(h))
          if atk_menu == 2:
            rand_dir = 'x'
            m.reveal(h.loc)
            while rand_dir == 'x':
              rand_num = randint(1,4)
              if rand_num == 1:
                rand_dir = h.go_north()
              elif rand_num == 2:
                rand_dir = h.go_south()
              elif rand_num == 3:
                rand_dir = h.go_east()
              elif rand_num == 4:
                rand_dir = h.go_west()
            m.reveal(h.loc)
            print("You ran away!")
        if e.hp == 0:
          print("You have slain a " + e.name)
          m.remove_at_loc(h.loc)
        if h.hp == 0:
          print("You have died.")
  
  
      #Healing Potion
      if dir == 'i':
        print("You found a health potion! You drink it to restore your health.")
        h.heal()
        m.remove_at_loc(h.loc)
  
      print()
  
      #Finish
      if m[h.loc[0]][h.loc[1]] == 'f':
        print("Congratulations! You found the stairs to the next floor of the dungeon.")
        counter += 1
        if counter > 3:
          counter = 1
        m.load_map(counter)
         
  print("Game Over")
        

main()