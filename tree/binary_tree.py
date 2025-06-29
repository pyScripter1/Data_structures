# Двоичние деревья - каждый узел имеет до двух потомков, левый дочерний узел и правый дочерний узел.
# Эта структура является основой для более сложных типов деревьев, таких как Binay Search Trees и AVL Trees.

# Это ограничение, согласно которому узел может иметь максимум два дочерних узла, дает нам множество преимуществ:
#
# Такие алгоритмы, как обход, поиск, вставка и удаление, становятся проще для понимания, реализуются и выполняются быстрее.
# Сортировка данных в двоичном дереве поиска (BST) делает поиск очень эффективным.
# Балансировку деревьев проще выполнять при ограниченном количестве дочерних узлов, например, используя двоичное дерево AVL.
# Двоичные деревья можно представить в виде массивов, что делает дерево более эффективным с точки зрения использования памяти.


# реализация двоичного дерева при помощи классов
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode("A")
treeNodeB = TreeNode("B")
treeNodeC = TreeNode("C")
treeNodeD = TreeNode("D")
treeNodeE= TreeNode("E")

root.left = treeNodeB
root.right = treeNodeC

treeNodeB.left = treeNodeD
treeNodeB.right = treeNodeE

print(root.left.right.data)


# Сбалансированное двоичное дерево имеет разницу между высотами левого и правого поддеревьев
# не более 1 для каждого узла дерева.
#
# Полное двоичное дерево имеет все уровни, заполненные узлами, за исключением последнего уровня,
# который также может быть заполнен или заполнен слева направо. Свойства полного двоичного дерева означают,
# что оно также сбалансировано .
#
# Полное двоичное дерево — это вид дерева, в котором каждый узел имеет либо 0, либо 2 дочерних узла .
#
# Идеальное двоичное дерево имеет все конечные узлы на одном уровне, что означает, что все уровни заполнены узлами,
# а все внутренние узлы имеют два дочерних узла. Свойства идеального двоичного дерева означают,
# что оно также является полным, сбалансированным и завершенным



# Обход двоичного дерева - посещение каждого узла дерева

# две основных категории обхода деревьев: Поиск в ширину и поиск в глубину
# Поиск в ширину (BFS) — это когда узлы на одном уровне посещаются перед переходом на следующий уровень в дереве.
# Это означает, что дерево исследуется в более боковом направлении.
#
# Поиск в глубину (DFS) — это процесс, при котором обход спускается по дереву до самых листовых узлов,
# исследуя ветвь за ветвью в нисходящем направлении.

# There are three different types of DFS traversals:
#
# pre-order
# in-order
# post-order

# Pre-order Traversal is a type of Depth First Search, where each node is visited in a certain order..
#
# Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree. It's used for creating a copy of the tree, prefix notation of an expression tree, etc.
#
# This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.
#
# This is how the code for pre-order traversal looks like:

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

preOrderTraversal(root)


# In-order Traversal is a type of Depth First Search, where each node is visited in a certain order.
#
# In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.
#
# What makes this traversal "in" order, is that the node is visited in between the recursive function calls. The node is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.
#
# This is how the code for In-order Traversal looks like:

print()
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

inOrderTraversal(root)


# Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order..
#
# Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.
#
# What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.
#
# This is how the code for Post-order Traversal looks like:
#
# Example

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")
print()
postOrderTraversal(root)




# bfs
from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Создание дерева
root = TreeNode("A")
treeNodeB = TreeNode("B")
treeNodeC = TreeNode("C")
treeNodeD = TreeNode("D")
treeNodeE = TreeNode("E")

root.left = treeNodeB
root.right = treeNodeC

treeNodeB.left = treeNodeD
treeNodeB.right = treeNodeE

# Обход дерева в ширину
print("Обход дерева в ширину (BFS):")
for level in bfs(root):
    print(level)

