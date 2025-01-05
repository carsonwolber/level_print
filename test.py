from tree import Tree
from node import Node

leaf_node_1 = Node(4)
leaf_node_2 = Node(5)
leaf_node_3 = Node(6)
leaf_node_4 = Node(7)

mid_node_1 = Node(2, leaf_node_1, leaf_node_2)
mid_node_2 = Node(3, leaf_node_3, leaf_node_4)

root_node = Node(1, mid_node_1, mid_node_2)

test_tree = Tree(root_node)

test_tree.print_level_traversal()