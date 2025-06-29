# A Linked List is, as the word implies, a list where the nodes are linked together.
# Each node contains data and a pointer.
# The way they are linked together is that each node points to where in the memory the next node is placed.

# Связанные списки не выделяются в памяти фиксированного размера, как массивы, поэтому связанным спискам не требуется перемещать весь список в больший объем памяти при заполнении фиксированного объема памяти, как это необходимо массивам.
# Узлы связанного списка не располагаются в памяти один за другим (непрерывно), поэтому узлы связанного списка не нужно сдвигать вверх или вниз в памяти при вставке или удалении узлов.
# Связанные списки узлов требуют больше памяти для хранения одной или нескольких ссылок на другие узлы. Элементы массива не требуют столько памяти, поскольку элементы массива не содержат ссылок на другие элементы.
# Операции со связанными списками обычно сложнее программировать и требуют больше строк, чем аналогичные операции с массивами, поскольку языки программирования имеют более эффективную встроенную поддержку массивов.
# Чтобы найти узел в определенной позиции, нам необходимо просмотреть связанный список, но с помощью массивов мы можем получить доступ к элементу напрямую, написав myArray[5] .

# Односвязный список — это простейший вид связанных списков.
# Он занимает меньше места в памяти, поскольку каждый узел имеет только один адрес к следующему узлу


class Node: # класс узел, узле хранит данные и указатель на следующий узел
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head): # обход односвязанного списка
    current_node = head
    while current_node:
        print(current_node.data, end="->")
        current_node = current_node.next
    print()

def find_lowest_value(head): # поиск наименьшего значения в односвязном списке
    min_value = head.data
    current_node = head
    while current_node:
        if min_value > current_node.data:
            min_value = current_node.data
        current_node = current_node.next
    return min_value


# Если вы хотите удалить узел в связанном списке,
# важно соединить узлы по обе стороны от узла перед его удалением,
# чтобы связанный список не был нарушен.
def delete_node(head, node_to_delete):
    if head == node_to_delete:
        return head.next
    current_node = head
    while current_node.next and current_node.next != node_to_delete:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next
    return head


# Вставка нового узла в связанный список.
# Чтобы вставить узел в связанный список, нам сначала нужно создать узел,
# а затем в месте, куда мы его вставим, нам нужно настроить указатели так,
# чтобы предыдущий узел указывал на новый узел,
# а новый узел указывал на правильный следующий узел.
def insert_new_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node
    current_node = head
    for _ in range(position - 2):
        if current_node is None:
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    return head


node1 = Node(5)
node2 = Node(11)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print(find_lowest_value(node1)) # выводим минимальное значение связанного списка
print_linked_list(node1) # выводим связанный список

node1 = delete_node(node1, node3) # удаляем узел3
print_linked_list(node1)

new_node = Node(97)
node1 = insert_new_node(node1, new_node, 2)
print_linked_list(node1)








