from random import randint
import enemy_factory
import easy_goblin
import easy_troll
import easy_ogre
class BeginnerFactory(enemy_factory.EnemyFactory):
  """Factory design class for beginner enemies."""
  def create_random_enemy(self):
    num = randint(1,3)
    if num == 1:
      return easy_goblin.EasyGoblin()
    if num == 2:
      return easy_troll.EasyTroll()
    if num == 3:
      return easy_ogre.EasyOgre()