import entity
from random import randint 
class EasyOgre(entity.Entity):
  """
  Represents an easy ogre
  
  Args:
    name (str): name of ogre
    max_hp (int): maximum hp of ogre
    hp (int): current hp of ogre
  """
  def __init__(self):
    """Initializes name, max_hp, and hp"""
    super().__init__("Ogre", randint(3,5))
    self._hp = self._max_hp

  def attack(self, entity):
    """Attacks an entity."""
    dmg = randint(1,4)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."

  