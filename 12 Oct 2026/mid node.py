# create a list of integers, find the middle node and delete node it.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

print("Original list:")
sll.display()

sll.delete_first()
print("After deleting first node:")
sll.display()

sll.delete_last()
print("After deleting last node:")
sll.display()
