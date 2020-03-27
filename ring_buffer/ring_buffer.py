from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            if self.storage.length == (self.capacity -1):
                self.current = self.storage.head
                self.storage.add_to_tail(item)
            else:
                self.storage.add_to_tail(item)
        elif self.storage.length == self.capacity:
            self.storage.tail.next = self.storage.head
            print("PREV", self.current.value)
            self.current.value = item
            print("NEW", self.current.value)
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        mover = self.storage.head
        list_buffer_contents.append(mover.value)
        print(self.storage.tail.value)
        while mover is not self.storage.tail:
            mover = mover.next
            list_buffer_contents.append(mover.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
