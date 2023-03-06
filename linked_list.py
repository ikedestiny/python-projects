class node:
  """
  An object for storing a single node of a linked list.
  Models two attributes - data and link to the next node in the list
  """
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
