class Node(object):
    def __init__(self, val):
        self.val = val
        self.hashset = set()
        self.left = None
        self.right = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(100000000)
        self.tail = Node(0)
        self.head.right, self.tail.left = self.tail, self.head
        self.hashmap = {}
        self.val_hashmap = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.hashmap:
            val = self.hashmap[key]
            self.hashmap[key] += 1
            node = self.val_hashmap[val]
            node.hashset.remove(key)
            if node.left.val != val + 1:
                new = Node(val + 1)
                self.insert_left(node, new)
                self.val_hashmap[val + 1] = new
            node.left.hashset.add(key)
            if len(node.hashset) == 0:
                self.delete_node(val)
        else:
            self.hashmap[key] = 1
            if self.tail.left.val != 1:
                new = Node(1)
                self.insert_left(self.tail, new)
                self.val_hashmap[1] = new
            self.tail.left.hashset.add(key)
            
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.hashmap:
            val = self.hashmap[key]
            if val == 1:
                self.tail.left.hashset.remove(key)
                del self.hashmap[key]
            else:
                node = self.val_hashmap[val]
                node.hashset.remove(key)
                self.hashmap[key] -= 1
                if node.right.val != val - 1:
                    new = Node(val - 1)
                    self.insert_left(node.right, new)
                    self.val_hashmap[val - 1] = new
                node.right.hashset.add(key)
            if len(self.val_hashmap[val].hashset) == 0:
                self.delete_node(val)
    
    def insert_left(self, old, new):
        new.left, new.right = old.left, old
        old.left.right, old.left = new, new
    
    def delete_node(self, val):
        node = self.val_hashmap[val]
        del self.val_hashmap[val]
        node.left.right, node.right.left = node.right, node.left
        
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.head.right == self.tail:
            return ''
        ret = self.head.right.hashset.pop()
        self.head.right.hashset.add(ret)
        return ret
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.tail.left == self.head:
            return ''
        ret = self.tail.left.hashset.pop()
        self.tail.left.hashset.add(ret)
        return ret

if __name__ == '__main__':
    s = AllOne()
    s.inc('a')
    s.inc('b')
    s.inc('b')
    s.inc('b')
    s.inc('b')
    s.dec('b')
    s.dec('b')
    print(s.getMaxKey())