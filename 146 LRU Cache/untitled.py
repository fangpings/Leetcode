class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.current = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.move_to_tail(node)
            return node.val
        else:
            return -1

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.move_to_tail(self.dic[key])
            self.dic[key].val = value
        else:
            node = Node(key, value)
            if self.current == self.capacity:
                self.remove(self.head.next)
                self.current -= 1
            self.current += 1
            self.dic[key] = node
            self.add(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dic[node.key]
        del node

    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev.next = node

    def move_to_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev.next = node


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))     
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))



