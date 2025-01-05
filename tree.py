from node import Node
import collections


class Tree:
  def __init__(self, root: Node):
    self.root = root

  def print_level_traversal(self):

    Q = collections.deque()
    Q.append(self.root)

    while Q: 
      level = []
      for _ in range(len(Q)):
        n = Q.popleft()
        level.append(n.val)

        if n.left:
          Q.append(n.left)

        if n.right:
          Q.append(n.right)
      self.print_level_helper(level)
  
  def print_level_helper(self, level):
    acc = ''
    for l in level:
      acc += str(l)
    print(acc)
      


        



