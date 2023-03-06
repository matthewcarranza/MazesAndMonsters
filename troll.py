import entity
from random import randint 
class Troll(entity.Entity):
  """
  Represents a difficult troll
  
  Args:
    name (str): name of troll
    max_hp (int): maximum hp of troll
    hp (int): current hp of troll
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    super().__init__("Tremendous Troll", randint(10,14))
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = randint(6,10)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."