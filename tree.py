from node import Node
import collections


class Tree:
  def __init__(self, root: Node):
    self.root = root

  def print_level_traversal(self):
    print(self.root.val, "\n")

    Q = collections.deque()
    Q.append(self.root)

    while Q: 
      level = []
      for _ in range(len(Q)):
        n = Q.popleft()

        if n.right:
          Q.append(n.right)
        if n.left:
          Q.append(n.left)
      self.print_level_helper(level)
  
  def print_level_helper(self, level):
    print(l + ' ' for l in level)
    print("\n")


        



