class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        if value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        if target == self.value:
            return True