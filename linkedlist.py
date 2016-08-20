class Node:

    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data


class LinkedList:

    def __init__(self, start=None):
        self.start = start

    def insert(self, data, pos=0):
        node = Node(data=data)
        if not self.start or pos==0:
            node.next = self.start
            self.start = node
        elif pos == -1:
            next = self.start
            while(next.next!=None):
                next = next.next
            next.next = node
        else:
            next = self.start
            for i in range(0, pos-1):
                if next:
                    next = next.next
            node.next = next.next
            next.next = node

    def print_list(self):
        next = self.start
        print "list"
        while(next!=None):
            print next.data
            next = next.next

    def __str__(self):
        s = ""
        p = self.start
        if p != None :
            while p:
                s += str(p.data)
                if p and p.next:
                    s += "-->"
                p = p.next

            return s

    def delete_from_list(self, data=None, pos=None):
        next = self.start
        if pos == 0 or self.start.data == data:
            self.start = self.start.next
            return

        if data:
            while next.next:
                if next.next.data==data:
                    next.next = next.next.next
                    break
                next = next.next

        elif pos:
            for i in range(0, pos-1):
                if next:
                    next = next.next
            if next.next:
                next.next = next.next.next

    def reverse_list(self):
        self._reverse_list(self.start)

    def _reverse_list(self, ptr):
        if not ptr.next:
            self.start = ptr
            return ptr
        else:
            print ptr.data
            ptr2 = self._reverse_list(ptr.next)
            ptr.next = None
            ptr2.next = ptr
            return ptr

    def reverse_in_pair(self):
        ptr = self.start
        prev = None
        while(ptr.next):
            temp = ptr.next
            ptr.next = ptr.next.next
            temp.next = ptr
            if prev:
                prev.next = temp
            else:
                self.start = temp
            prev = ptr
            ptr = ptr.next


class DNode:

    def __init__(self, next=None,prev=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data


class DoublyLinkedList:

    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def insert(self, data, pos=0):
        node = DNode(data=data)
        if not self.head or pos==0:
            node.next = self.head
            self.head = node
            self.end = node
        elif pos == -1:
            next = self.head
            while(next.next!=None):
                next = next.next
            node.prev = next
            next.next = node
            self.end = node
        else:
            next = self.head
            count = 0
            while next and count != pos-1:
                count += 1
                next = next.next
            if count==pos-1:
                node.next = next.next
                if next.next:
                    next.next.prev = node
                else:
                    self.end = node
                node.prev = next
                next.next = node

    def __str__(self):
        s = ""
        p = self.head
        if p != None :
            while p:
                s += str(p.data)
                if p and p.next:
                    s += "-->"
                p = p.next

            return s

    def traverse_from_end(self):
        s = ""
        p = self.end
        if p != None :
            while p:
                s += str(p.data)
                if p and p.prev:
                    s += "-->"
                p = p.prev

            return s

    def delete_from_list(self, data=None, pos=None):
        next = self.head
        if pos == 0 or self.head.data == data:
            self.head = self.head.next
            return

        if data:
            while next.next:
                if next.next.data==data:
                    next.next = next.next.next
                    if next.next.next:
                        next.next.next.prev = next
                    break
                next = next.next

        elif pos:
            count = 0
            while next and count != pos-1:
                count += 1
                next = next.next
            if count == pos-1:
                next.next = next.next.next
                if next.next.next:
                    next.next.next.prev = next

    def n_th_node_from_end(self, n):
        ptr1 = self.head
        ptr2 = self.head

        for i in range(0, n-1):
            ptr1 = ptr1.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr2.data



list = LinkedList()
print "inserting 1"
list.insert(1)
print list

print "inserting 2"
list.insert(2, 1)
print list

print "inserting 3 at end"
list.insert(3, -1)
print list

print "inserting 4 at position 2"
list.insert(4, -1)
list.insert(5, -1)
list.insert(6, -1)
list.insert(7, -1)
list.insert(8, -1)
list.insert(9, -1)
list.insert(10, -1)
list.insert(11, -1)
print list

#list.reverse_list()
list.reverse_in_pair()
print list

# list.traverse_from_end()

#
# print list.n_th_node_from_end(9)

# print "inserting 2"
# list.delete_from_list(2)
# print list









