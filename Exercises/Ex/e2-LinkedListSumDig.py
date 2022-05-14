# Linked List Node
class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

# Handle list operations


class LinkedList:

    def __init__(self):

        self.head = None

    # Method to traverse list and
    # return it in a format
    def traverse(self):

        linkedListStr = ""
        temp = self.head

        while temp:
            linkedListStr += str(temp.data) + " -> "
            temp = temp.next

        return linkedListStr + "NULL"

    # Method to insert data in linked list
    def insert(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

# Helper function to reverse the list


def reverse(Head):

    if (Head is None and Head.next is None):
        return None

    prev = None
    curr = Head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    Head = prev
    return Head

# Function to add two lists


def listSum(l1, l2):

    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Reverse first list
    l1 = reverse(l1)

    # Reverse second list
    l2 = reverse(l2)

    # Storing head whose reverse is to be returned This is where which will be final node
    head = l1
    prev = None
    c = 0
    sum = 0

    # As long as the lists are the same length
    while l1 is not None and l2 is not None:
        sum = c + l1.data + l2.data
        l1.data = sum % 10
        c = int(sum / 10)
        prev = l1
        l1 = l1.next
        l2 = l2.next

    # If left in list 1 or 2
    if l1 is not None or l2 is not None:
        if l2 is not None:
            prev.next = l2
        l1 = prev.next

        while l1 is not None:
            sum = c + l1.data
            l1.data = sum % 10
            c = int(sum / 10)
            prev = l1
            l1 = l1.next

    # The rest of the division remains
    if c > 0:
        prev.next = Node(c)

    return reverse(head)


def listSumNewList(l1, l2):

    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Reverse first list
    l1 = reverse(l1)

    # Reverse second list
    l2 = reverse(l2)

    # Storing head whose reverse is to be returned This is where which will be final node

    c = 0
    sum = 0
    sumLists = LinkedList()
    head = l1

    # As long as the lists are the same length
    while l1 is not None and l2 is not None:
        sum = c + l1.data + l2.data
        sumLists.insert(sum % 10)
        c = int(sum / 10)
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        sum = c + l1.data
        sumLists.insert(sum % 10)
        c = int(sum / 10)
        l1 = l1.next

    while l2 is not None:
        sum = c + l2.data
        sumLists.insert(sum % 10)
        c = int(sum / 10)
        l2 = l2.next

    # The rest of the division remains
    if c > 0:
        sumLists.insert(c)

    return reverse(sumLists.head)


# Driver code
linkedList1 = LinkedList()
linkedList1.insert(3)
linkedList1.insert(5)
# 53
print('linkedList1:', linkedList1.traverse())

linkedList2 = LinkedList()
linkedList2.insert(2)
linkedList2.insert(6)
linkedList2.insert(8)
# 862
print('linkedList2:', linkedList2.traverse())


linkedList3 = LinkedList()

linkedList3.head = listSumNewList(linkedList1.head, linkedList2.head)
print('linkedList3', linkedList3.traverse())


# linkedList3.head = listSum(linkedList1.head, linkedList2.head)
# print('linkedList3', linkedList3.traverse())

# linkedList1: 5 -> 3 -> NULL
# linkedList2: 8 -> 6 -> 2 -> NULL
# linkedList3 9 -> 1 -> 5 -> NULL
