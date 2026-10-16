# 2601196 - Ashutosh Uttekar 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Traverse and print the node values
    def traverse(self):
        if not self.head:
            print("Linked list is empty.")
            return
        
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position
    # doing at- (1-based index)
    def insert_at_position(self, data, position):
        new_node = Node(data)

        # If inserting at the head (Position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        # Traverse to the node just before the required position
        for _ in range(1, position - 1):
            if temp is None:
                break
            temp = temp.next

        # If position is out of bounds
        if temp is None:
            print("Position out of bounds.")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete alternate nodes in the linked list
    def delete_alternate(self):
        if not self.head:
            return

        prev = self.head
        node_to_delete = self.head.next

        while prev and node_to_delete:
            # Bypass the node to be deleted
            prev.next = node_to_delete.next
            
            """Python handles garbage collection automatically, so we just move the pointers forward."""
            prev = prev.next
            if prev:
                node_to_delete = prev.next

#Executionm Block -
if __name__ == "__main__":
    llist = LinkedList()

    print(" 1. Creating Linked List (Appending 10, 20, 30, 40, 50)")
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.append(50)
    
    print("\n 2. Traversing and printing the node values")
    llist.traverse()

    print("\n 3. Inserting node with value 25 at position 3")
    llist.insert_at_position(25, 3)
    llist.traverse()

    print("\n 3b. Inserting node with value 5 at position 1 (Head)")
    llist.insert_at_position(5, 1)
    llist.traverse()

    print("\n 4. Deleting alternate nodes")
    llist.delete_alternate()
    llist.traverse()

