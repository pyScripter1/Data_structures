# Двоичное дерево поиска — это двоичное дерево, в котором левый дочерний элемент каждого узла имеет меньшее значение,
# а правый дочерний элемент каждого узла имеет большее значение.
#
# Явным преимуществом двоичных деревьев поиска является то, что такие операции,
# как поиск, удаление и вставка, выполняются быстро и без необходимости сдвига значений в памяти.

# Двоичное дерево поиска (BST) — это тип структуры данных двоичного дерева , в котором для любого узла «X» в дереве должны выполняться следующие свойства:
#
# Левый дочерний элемент узла X и все его потомки (дочерние элементы, дочерние элементы дочерних элементов и т. д.) имеют значения, меньшие значения X.
# Правый дочерний элемент и все его потомки имеют более высокие значения, чем значение X.
# Левое и правое поддеревья также должны быть бинарными деревьями поиска.
# Эти свойства ускоряют поиск, добавление и удаление значений по сравнению с обычным бинарным деревом.
#
# Чтобы сделать это максимально простым для понимания и реализации, давайте также предположим, что все значения в двоичном дереве поиска уникальны.
#
# Размер дерева — это количество узлов в нем(n) .
#
# Поддерево начинается с одного из узлов дерева в качестве локального корня и состоит из
# этого узла и всех его потомков .
#
# Потомками узла являются все дочерние узлы этого узла и все их дочерние узлы и т. д.
# Просто начните с узла, и потомками будут все узлы, которые соединены ниже этого узла .
#
# Высота узла — это максимальное количество ребер между этим узлом и листовым узлом.
#
# Преемником узла в порядке следования является узел, который следует за ним,
# если мы делаем обход в порядке следования. Обход BST в порядке следования выше приведет к тому,
# что узел 13 будет предшествовать узлу 14, и поэтому преемником узла 13 будет узел 14.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(node): # Обход двоичного дерева поиска
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end = " ")
    in_order_traversal(node.right)

# поиск элемента в двоичном дереве поиска
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    elif target > node.data:
        return search(node.right, target)

# втсавка узла в двоичное дерево поиска
def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

# нахождение наименьшего занчение в ДДП
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# нахождение наибольшего значения в ДДП
def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


# Чтобы удалить узел, наша функция должна сначала выполнить поиск в BST, чтобы найти его.
#
# После того, как узел найден, есть три различных случая, когда удаление узла должно выполняться по-разному.

# Как это работает:
#
# Если узел является листовым, удалите его, удалив ссылку на него.
# Если у узла есть только один дочерний узел, соедините родительский узел узла, который вы хотите удалить, с этим дочерним узлом.
# Если у узла есть как правый, так и левый дочерние узлы: найдите преемника узла по порядку, измените значения с этим узлом, затем удалите его.


def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else: # узел только с одним ребенком или без него вовсе
        if not node.left:
            temp = node.left
            node = None
            return temp
        elif not node.right:
            temp = node.right
            noe = None
            return temp

        # узел с двумя ребенками
        node.data = find_min(node.right).data
        node.right = delete(node.right, node.data)
    return node


root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

in_order_traversal(root) # Обход дерева
print()
result = search(root, 187)
if result:
    print(f"found {result.data}")
else:
    print("Not found")

insert(root, 10) # втсавка нового узла
in_order_traversal(root)

print(f"Min = {find_min(root).data}")
print(f"Max = {find_max(root).data}")

# delete node 15
delete(root, 15)

in_order_traversal(root)










