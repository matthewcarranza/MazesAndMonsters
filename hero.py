import entity
import random
import map
class Hero(entity.Entity):
  """
  Represents a hero
  
  Args:
    name (str): name of hero
    max_hp (int): maximum hp of hero
    hp (int): current hp of hero
    loc (list): current location of hero
  """
  def __init__(self, name, max_hp):
    """Initializes name, max_hp, hp, and loc"""
    super().__init__(name, max_hp)
    self._hp = self._max_hp
    self._loc = [0, 0]

  def attack(self, entity):
    """Attacks an entity."""
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    return self.name + " attacks a " + entity.name + " for " + str(dmg) + " damage."

  @property
  def loc(self):
    """Getter for loc."""
    return self._loc

  def go_north(self):
    """Hero travels north."""
    if self.loc[0] > 0:
      self.loc[0] -= 1
      return map.Map()[self.loc[0]][self.loc[1]]
    return 'x'
    
  def go_south(self):
    """Hero travels south."""
    if self.loc[0] < len(map.Map()[0])-1:
      self.loc[0] += 1
      return map.Map()[self.loc[0]][self.loc[1]]
    return 'x'
    
  def go_east(self):
    """Hero travels east."""
    if self.loc[1] < len(map.Map())-1:
      self.loc[1] += 1
      return map.Map()[self.loc[0]][self.loc[1]]
    return 'x'
    
  def go_west(self):
    """Hero travels west."""
    if self.loc[1] > 0:
      self.loc[1] -= 1
      return map.Map()[self.loc[0]][self.loc[1]]
    return 'x'