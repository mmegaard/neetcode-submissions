class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def print_list(self) -> None:
        list_string = ''
        temp = self.head
        while temp:
            list_string += f'<- |{temp.val}| -> '
            temp = temp.next
        print(list_string)

    def get_prev_node(self, index: int) -> ListNode:
        if index <= self.size/2:
            head = self.head
            for _ in range(index):
                head = head.next
            return head
        else:
            tail = self.tail
            for _ in range(self.size - index + 1):
                tail = tail.prev
            return tail

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.get_prev_node(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        new_node = ListNode(val)
        prev = self.get_prev_node(index)
        next_node = prev.next
        new_node.prev = prev
        prev.next = new_node
        new_node.next = next_node
        next_node.prev = new_node
        self.size +=1
        self.print_list()

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.get_prev_node(index)
        to_delete = prev.next
        next_node = to_delete.next
        prev.next = next_node
        next_node.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)