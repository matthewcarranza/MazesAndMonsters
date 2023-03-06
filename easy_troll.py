import entity
from random import randint 
class EasyTroll(entity.Entity):
  """
  Represents an easy troll
  
  Args:
    name (str): name of troll
    max_hp (int): maximum hp of troll
    hp (int): current hp of troll
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    super().__init__("Troll", randint(4,5))
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = randint(1,5)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."

  