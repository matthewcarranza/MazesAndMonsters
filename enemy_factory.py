import abc
class EnemyFactory(abc.ABC):
  """Interface for creating enemies."""
  @abc.abstractmethod
  def create_random_enemy(self):
    pass