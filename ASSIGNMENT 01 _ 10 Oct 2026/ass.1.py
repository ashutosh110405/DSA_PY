class Node:
    """Class to represent a node in the Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List / Append Node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 2. Traverse and print the node values
    def traverse(self):
        if not self.head:
            print("Linked List is empty.")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    # 3. Insert node at a specific position (0-indexed)
    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        # Inserting at the head (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next
            
        if current is None:
            print("Position out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node

    # 4. Find Middle node and print its value (Using Tortoise and Hare algorithm)
    def find_middle(self):
        if not self.head:
            print("List is empty, no middle node.")
            return None
            
        slow = self.head
        fast = self.head
        
        # Fast pointer moves 2 steps, slow pointer moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        print(f"Middle node value: {slow.data}")
        return slow.data

    # 5. Delete node (by value)
    def delete_node(self, key):
        current = self.head

        # Case 1: If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Case 2: Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not present in the linked list
        if current is None:
            print(f"Node with value {key} not found.")
            return

        # Unlink the node from linked list
        prev.next = current.next
        current = None

    # 6. Reverse list
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev and current one step forward
            current = next_node
            
        self.head = prev

    # 7. Calculate the sum of every two consecutive node values
    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sums.")
            return
            
        sums = []
        current = self.head
        
        while current.next:
            consecutive_sum = current.data + current.next.data
            sums.append(consecutive_sum)
            current = current.next
            
        print("Sum of consecutive nodes:", sums)

# ==========================================
# Driver Code to test the operations
# ==========================================
if __name__ == "__main__":
    ll = LinkedList()
    
    print("1 & 2. Creating and Traversing Linked List:")
    for val in [10, 20, 30, 40, 50]:
        ll.append(val)
    ll.traverse()
    
    print("\n3. Inserting 25 at position 2:")
    ll.insert_at_position(25, 2)
    ll.traverse()
    
    print("\n4. Finding Middle Node:")
    ll.find_middle()
    
    print("\n5. Deleting node 30:")
    ll.delete_node(30)
    ll.traverse()
    
    print("\n6. Reversing List:")
    ll.reverse()
    ll.traverse()
    
    print("\n7. Calculating sum of consecutive nodes:")
    ll.sum_consecutive()
