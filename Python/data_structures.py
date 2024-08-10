import heapq
import collections


# A stack is structured to be peekable only at its beginning and end.
# useful for sorting and retrieving data in reverse order


class Stack(list):
    def __init__(self):
        super().__init__()
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_string_with_stack(str1):
    s = Stack()
    rev_str = ''
    for c in str1:
        s.push(c)
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


# We can implement a stack with nodes
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

    def get_date(self):
        return self.value

    def get_next(self):
        return self.next

    def set_date(self, new_data):
        self.value = new_data

    def set_next(self, new_next):
        self.next = new_next


class NodeStack(object):
    def __init__(self):
        self.top = None

    def is_empty(self):
        return bool(self.top)

    def pop(self):
        node = self.top
        if node:
            self.top = node.next.next
            return node.value
        else:
            raise Exception("Stack is empty")

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node.next

    def size(self):
        node = self.top
        if node is not None:
            num_nodes = 1
        else:
            return 0
        node = node.next
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peek(self):
        return self.top.value


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception('Queue is empty.')


class QueueTwoLists(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise Exception("Queue empty!")
        return self.out_stack.pop()

    def size(self):
        if self.out_stack:
            return self.out_stack[-1]
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return None


class Dequeue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "{}".format(self.items)


class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data) // 2, -1, -1):
            self.__max__heapify__(i)

    def __repr__(self):
        return '{}'.format(self.data)

    def parent(self, i):
        return i >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def __max__heapify__(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)
        largest = (left < n and self.data[left]) > self.data[i] and left or i
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], \
                self.data[i]
            self.__max__heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max__heapify__(0)
        return max_element


class PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node(self, value):
        temp = self.head
        node = Node(value)
        node.next = temp
        self.head = node
        self.length += 1

    def print_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def delete_node(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if index == i:
            self.length -= 1
            if prev is None:
                self.head = node.next
            else:
                prev.next = node.next
        else:
            print('Index not found')


# a FIFO linked list

class LinkListFIFO(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def print_list(self):
        node = self.head.next
        while node:
            print(node.value)
            node = node.next_node

    def delete_node(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if i == index:
            if not prev:
                self.head = node.next
            else:
                prev.next = node.next
            self.length -= 1
        else:
            print("Index not found!")

    def remove_dupl(self):
        prev = None
        node = self.head
        aux_dict = collections.Counter()
        while node:
            value_here = node.value
            if aux_dict[value_here] == 0:
                aux_dict[value_here] = 1
            else:
                prev.next = node.next
            self.length -= 1
        prev = node
        node = node.next
