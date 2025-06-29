# Причины реализации стеков с использованием списков/массивов:
#
# Эффективное использование памяти: элементы массива не содержат адрес следующего элемента, как узлы связанного списка.
# Проще реализовать и понять: использование массивов для реализации стеков требует меньше кода, чем использование связанных списков, и по этой причине его обычно проще понять.
# Причина, по которой не следует использовать массивы для реализации стеков:
#
# Фиксированный размер: Массив занимает фиксированную часть памяти. Это означает, что он может занять больше памяти, чем нужно, или если массив заполнится, он не сможет вместить больше элементов.


# Stack Implementation using Linked Lists
# A linked list consists of nodes with some sort of data, and a pointer to the next node.

# Большим преимуществом использования связанных списков является то,
# что узлы хранятся везде, где есть свободное место в памяти,
# узлы не должны храниться последовательно друг за другом, как элементы хранятся в массивах.
# Еще одна приятная вещь связанных списков заключается в том,
# что при добавлении или удалении узлов, остальные узлы в списке не должны сдвигаться.


# class of node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # pointer on next node

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value) # create new node
        if self.head: # if have head, than create pointer on head
            new_node.next = self.head
        self.head = new_node # if no head, create it else change head
        self.size += 1 # increase size

    def pop(self):
        if self.is_empty(): # if empty - exception
            raise Exception("Stack is empty")
        popped_node = self.head # else pop element
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def stack_size(self):
        return self.size

    def traverseAndPrint(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print()

    def is_empty(self):
        return self.size == 0


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print("LinkedList = ", end="")
my_stack.traverseAndPrint()
print("Peek", my_stack.peek())
print("Pop", my_stack.pop())
print("LinkedList after pop", end=" ")
my_stack.traverseAndPrint()
print("isEmpty:", my_stack.is_empty())
print("Size:", my_stack.stack_size())

# Причина использования связанных списков для реализации стеков:
#
# Динамический размер: стек может динамически увеличиваться и уменьшаться, в отличие от массивов.
# Причины, по которым не следует использовать связанные списки для реализации стеков:
#
# Дополнительная память: каждый элемент стека должен содержать адрес следующего элемента (следующего узла связанного списка).
# Читаемость: Некоторым может быть сложнее читать и писать код, поскольку он длиннее и сложнее.

# Распространенные приложения стека
# Стеки используются во многих реальных сценариях:
#
# Отмена/Повтор операций в текстовых редакторах
# История браузера (назад/вперед)
# Стек вызовов функций в программировании
# Оценка выражения

