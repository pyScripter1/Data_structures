# Двусвязный список имеет узлы с адресами как к предыдущему,
# так и к следующему узлу, как на изображении ниже, и поэтому занимает больше памяти.
# Но двусвязные списки хороши,
# если вы хотите иметь возможность перемещаться как вверх, так и вниз по списку.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # сслыка на след узел
        self.prev = None # ссылка на предыдущий узел


node1 = Node(90)
node2 = Node(12)
node3 = Node(83)
node4 = Node(74)
node5 = Node(19)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

