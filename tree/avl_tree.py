# AVL - дерево — это тип двоичного дерева поиска, названный в честь двух советских изобретателей
# Георгия Андресона - Вельского и Евгения Ландиса , которые изобрели AVL-дерево в 1962 году.
#
# Деревья AVL являются самобалансирующимися, что означает, что высота
# дерева поддерживается на минимальном уровне, что гарантирует очень быстрое время выполнения для поиска, вставки и удаления узлов, с временной сложностью
# О (log n)

# Единственное различие между обычным двоичным деревом поиска и AVL-деревом заключается в том,
# что AVL-деревья дополнительно выполняют операции вращения для сохранения баланса дерева.
#
# Двоичное дерево поиска находится в равновесии, когда разница в высоте между левым и правым поддеревьями составляет менее 2.
#
# Сохраняя баланс, AVL-дерево обеспечивает минимальную высоту дерева, что означает,
# что операции поиска, вставки и удаления могут выполняться очень быстро.

# реализация AVL деревьев
# По сравнению с BST в дереве AVL появился только один новый атрибут для каждого узла
# — это высота, но для реализации дерева AVL
# требуется много новых функций и дополнительных строк кода из-за особенностей балансировки дерева AVL.

# Баланс-фактор (Balance Factor, BF) для узла X — это разница между высотой его правого и левого поддеревьев.
# BF(X) = height(rightSubtree(X)) - height(leftSubtree(X))
# Значения баланс-фактора:
#
# 0: Узел сбалансирован.
#
# > 0: Узел "перевешивает вправо" (right heavy).
#
# < 0: Узел "перевешивает влево" (left heavy).
#
# Если баланс-фактор какого-либо узла дерева выходит за пределы диапазона [-1, 1] (то есть меньше -1 или больше 1),
# дерево считается несбалансированным, и для восстановления баланса требуется выполнить операцию поворота (rotation).

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

def getHeight(node):
  if not node:
    return 0
  return node.height

def getBalance(node):
  if not node:
    return 0
  return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
  print('Rotate right on node',y.data)
  x = y.left
  T2 = x.right
  x.right = y
  y.left = T2
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  return x

def leftRotate(x):
  print('Rotate left on node',x.data)
  y = x.right
  T2 = y.left
  y.left = x
  x.right = T2
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  return y

def insert(node, data):
  if not node:
    return TreeNode(data)

  if data < node.data:
    node.left = insert(node.left, data)
  elif data > node.data:
    node.right = insert(node.right, data)

  # Update the balance factor and balance the tree
  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and getBalance(node.left) >= 0:
    return rightRotate(node)

  # Left Right
  if balance > 1 and getBalance(node.left) < 0:
    node.left = leftRotate(node.left)
    return rightRotate(node)

  # Right Right
  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)

  # Right Left
  if balance < -1 and getBalance(node.right) > 0:
    node.right = rightRotate(node.right)
    return leftRotate(node)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

# Inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)


# Реализация удаления узла AVL
# При удалении узла, который не является листовым узлом, AVL Tree требует,
# minValueNode()чтобы функция нашла следующий узел узла в упорядоченном обходе.
# Это то же самое, что и при удалении узла в Binary Search Tree, как объяснялось на предыдущей странице.
#
# Для удаления узла в дереве AVL необходим тот же код восстановления баланса, что и для кода вставки узла.


def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return node

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    if node.left is None:
      temp = node.right
      node = None
      return temp
    elif node.right is None:
      temp = node.left
      node = None
      return temp

    temp = minValueNode(node.right)
    node.data = temp.data
    node.right = delete(node.right, temp.data)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

# Inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)




