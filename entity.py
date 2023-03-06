import abc
class Entity(abc.ABC):
  """
  Represents an entity.
  
  Args:
    name (str): name of entity
    max_hp (int): maximum hp of entity
    hp (int): current hp of entity
  """
  def __init__(self, name, max_hp):
    """Initializes name, max_hp, and hp"""
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    """Getter for name."""
    return self._name

  @property
  def hp(self):
    """Getter for hp."""
    return self._hp
  
  def take_damage(self, dmg):
    """Has entity take damage."""
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0
    
  def heal(self):
    """Heals entity."""
    self._hp = self._max_hp

  def __str__(self):
    """Entity and health in string format."""
    return str(self._name) + "\nHP: " + str(self._hp) + "/" + str(self._max_hp)

  @abc.abstractmethod
  def attack(self, entity):
    pass