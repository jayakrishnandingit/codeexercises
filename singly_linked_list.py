#!/usr/bin/python3

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListError(Exception):
    pass


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Insert at the front.
        One of the reasons of existence of linked lists.
        Time complexity: O(1).
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, node, data):
        """
        Insert a node after a node.
        Time complexity: O(1).
        """
        if not node:
            raise LinkedListError("Node to insert after cannot be empty.")

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def append(self, data):
        """
        Append a node to the linked list.
        Time complexity: O(n).
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete_node(self, data):
        if self.head is None:
            raise LinkedListError("Empty list.")

        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next
            if temp is not None:
                prev.next = temp.next
            else:
                # data not found.
                raise LinkedListError("Node with data %s not found." % data)

    def reverse(self):
        prev = None
        current = self.head
        nxt = None

        if self.head is None:
            raise LinkedListError("Empty list.")

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        next_node = self.head
        while next_node:
            print("%s->" % next_node.data)
            next_node = next_node.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(6)
    llist.append(7)
    llist.insert_after(llist.head, 8)
    llist.insert_after(llist.head.next, 1)
    print("Print after insert.")
    llist.print_list()

    llist.delete_node(8)
    print("deleted a node.")
    llist.print_list()
    
    llist.push(9)
    print("added a new head.")
    llist.print_list()
    llist.reverse()
    print("reversed the list.")
    llist.print_list()    
