import entity
from random import randint 
class Ogre(entity.Entity):
  """
  Represents a difficult ogre
  
  Args:
    name (str): name of ogre
    max_hp (int): maximum hp of ogre
    hp (int): current hp of ogre
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    super().__init__("Lumbering Ogre", randint(8,12))
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = randint(6,10)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."