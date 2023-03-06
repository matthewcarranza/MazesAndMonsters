class Map:
  """
  Represents the map of the game.
  
  Args:
    map (2D list): game map
    revealed (2D list): list of revealed or unrevealed locations determined by being True or False
  """
  _instance = None
  _initialized = False

  def __new__(cls, *args):
    """Constructs map if it hasn't been constructed already."""
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """Initializes map and revealed if they haven't been initialized already."""
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True


  def __getitem__(self, row):
    """Returns the row specified from map."""
    return self._map[row]

  def __len__(self):
    """Returns the length of map (row or column)."""
    return len(self._map)

  def load_map(self, map_num):
    """Reads map file to create the map 2D list and sets all the revealed list elements to False."""
    if map_num == 1:
      self._file = open("map1.txt")
    if map_num == 2:
      self._file = open("map2.txt")
    if map_num == 3:
      self._file = open("map3.txt")
    
    self._file = self._file.read()
    self._file = self._file.replace("\n", "")
    self._map = []
    
    for i in range(5):
      self._templist = []
      for j in range(5):
        self._templist.append(str(self._file)[j+5*i:j+1+5*i])
      self._map.append(self._templist)

    self._revealed = [[False for x in range(len(self._map[0]))] for y in range(len(self._map))]
    return 0

  def show_map(self, loc):
    """Displays map."""
    str = ""
    for row in range(len(self._map)):
      for col in range(len(self._map[0])):
        if row == loc[0] and col == loc[1]:
          str += '* '
        elif self._revealed[row][col] is True:
          str += self._map[row][col] + " "
        else:
          str += 'x '
      str+= "\n"
    
    return str

  def reveal(self, loc):
    """Sets the specified location on the revealed map to True."""
    self._revealed[loc[0]][loc[1]] = True
    return 0

  def remove_at_loc(self, loc):
    """Overwrites the character in the map list at the specified location with an ‘n’."""
    self._map[loc[0]][loc[1]] = 'n'
    return 0
      
      
    
    