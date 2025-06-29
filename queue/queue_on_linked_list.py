# Приумущество использовать связанные списки вместо массивов в том, что узлы хранятся везде где есть
# свободная помять, а не последовательно как элементы массивов. Еще при добавлении или удалении элементов
# остальные узлы не должны двигаться


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None # first element in queue
        self.rear = None # last added element in queue
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.value, end = "->")
            temp = temp.next
        print()


my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.printQueue()

print(my_queue.peek())
print(my_queue.dequeue())
my_queue.printQueue()

# Причины использования связанных списков для реализации очередей:
#
# Динамический размер: очередь может динамически увеличиваться и уменьшаться, в отличие от массивов.
# Без сдвига: передний элемент очереди можно удалить (поставить в очередь) без необходимости сдвига других элементов в памяти.
# Причины, по которым не следует использовать связанные списки для реализации очередей:
#
# Дополнительная память: каждый элемент очереди должен содержать адрес следующего элемента (следующего узла связанного списка).
# Читаемость: Некоторым может быть сложнее читать и писать код, поскольку он длиннее и сложнее.



# Приложения общей очереди
# Очереди используются во многих реальных сценариях:
#
# Планирование задач в операционных системах
# Поиск в ширину в графах
# Очереди сообщений в распределенных системах






