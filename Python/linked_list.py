class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_cargo(self):
        return self.value

    def get_next(self):
        return self.next

    def set_cargo(self, c):
        self.value = c

    def set_next(self, n):
        self.next = n

    def __str__(self):
        return(str(self.value))

    def remove_second(self, lst):
        if not lst:
            return
        first = lst
        second = lst.get_next()
        first.set_next(second.get_next())
        second.set_next(None)
        return second

    def print_backward(firstnode):
        output = print_backward_helper(firstnode)
        lstbwkd = "[" + output[:len(output) - 2 + "]"
        print(lstbwkd)

class LinkedList(object):
    def __init__(self):
        self.length= 0
        self.head= None

    def add_first(self, cargo):
        node= Node(cargo)
        node.set_next(self.head)
        self.head= node
        self.length= self.length + 1

    def print_backward_helper(self, curr):
        if not curr:
            return ""
        else:
            head= curr
            tail= curr.get_next()
            return self.print_backward_helper(tail) + str(head) + ", "

    def print_backward(self):
        output= self.print_backward_helper(self.head)
        lstbwkd= "[" + output[:len(output) - 2 + "]"
        print(lstbwkd)
