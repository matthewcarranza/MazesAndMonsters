from random import randint
import enemy_factory
import goblin
import troll
import ogre
class ExpertFactory(enemy_factory.EnemyFactory):
  """Factory design class for expert enemies."""
  def create_random_enemy(self):
    num = randint(1,3)
    if num == 1:
      return goblin.Goblin()
    if num == 2:
      return troll.Troll()
    if num == 3:
      return ogre.Ogre()