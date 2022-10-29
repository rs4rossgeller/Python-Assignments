class Node:
    """_summary_ : Linked List Node class"""

    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


def detect_loop(head: Node) -> bool:
    """_summary_ : Detects if a loop exists in a linked list"""
    slow_pointer: Node = head
    fast_pointer: Node = head

    while (
        slow_pointer is not None
        and fast_pointer is not None
        and fast_pointer.next is not None
    ):
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True

    return False


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    # Graph with no Loops
    if detect_loop(head):
        print("Loop found")
    else:
        print("No Loop")

    # Graph with Loops
    print("Creating a loop for testing")
    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = head

    if detect_loop(head):
        print("Loop found")
    else:
        print("No Loop")
