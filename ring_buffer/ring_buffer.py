from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            current = self.storage.head
        elif len(self.storage) == self.capacity and current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            current = self.storage.next
        elif len(self.storage) == self.capacity:
            gone = current
            current = self.storage.next
            self.storage.insert_before(gone)
            delete


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        mover = self.storage.head
        list_buffer_contents.append(mover.value)
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
