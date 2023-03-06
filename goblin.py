import entity
from random import randint 
class Goblin(entity.Entity):
  """
  Represents a difficult goblin
  
  Args:
    name (str): name of goblin
    max_hp (int): maximum hp of goblin
    hp (int): current hp of goblin
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    super().__init__("Vicious Goblin", randint(6,10))
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = randint(4,8)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."

  