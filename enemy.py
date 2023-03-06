import entity
import random
class Enemy(entity.Entity):
  """
  Represents an enemy
  
  Args:
    name (str): name of enemy
    max_hp (int): maximum hp of enemy
    hp (int): current hp of enemy
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    names = ['Goblin', 'Troll', 'Ghoul', 'Skeleton', 'Kobold']
    self._name = names[random.randrange(0,len(names))]
    self._max_hp = random.randint(4,8)
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."

  
    