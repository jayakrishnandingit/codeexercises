class Node():
    """
    Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

    Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
    You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
    """
    def __init__(self, value):
        self.state = 'unlocked'
        self.left = None
        self.right = None
        self.parent = None

    def is_locked(self):
        return self.state == 'locked'

    def parent_is_locked(self):
        if self.parent:
            if self.parent.is_locked():
                return True
            return self.parent.parent_is_locked()
        else:
            return self.is_locked()

    def is_descendant_locked(self):
        if not self.left and not self.right:
            return False

        queue = [self.left, self.right]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.is_locked():
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def lock(self):
        if self.is_locked():
            return False
        if self.parent_is_locked():
            return False
        if self.is_descendant_locked():
            return False
        sellf.state = 'locked'
        return True

    def unlock(self):
        pass
