from collections import defaultdict

class DoubleLikedList(object):
    """docstring for DoubleLikedList"""
    def __init__(self, key, val):
        self.val = val
        self.freq = 0
        self.key = key
        self.left = None
        self.right = None
        

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.hash_node = defaultdict(list)
        self.hash_frequency = defaultdict(list)
        self.end = DoubleLikedList(0, 0)
        self.head = DoubleLikedList(0, 0)
        self.end.left, self.head.right = self.head, self.end
        self.end.freq = -1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_node:
            return -1
        node = self.hash_node[key]
        freq = node.freq
        if node == self.hash_frequency[freq]:
            if node.right.freq == freq:
                self.hash_frequency[freq] = node.right
            else:
                self.hash_frequency[freq] = None
            if self.hash_frequency[freq + 1]:
                self.delete_node(node)
                self.insert_left(self.hash_frequency[freq + 1], node)
        else:
            self.delete_node(node)
            if not self.hash_frequency[freq + 1]:
                self.insert_left(self.hash_frequency[freq], node)
            else:
                self.insert_left(self.hash_frequency[freq + 1], node)
        node.freq += 1
        self.hash_frequency[freq + 1] = node
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity:
            if key not in self.hash_node:
                if self.count == self.capacity:
                    evict = self.end.left
                    self.delete_node(evict)
                    self.hash_node.pop(evict.key)
                    if self.hash_frequency[evict.freq] == evict:
                        self.hash_frequency[evict.freq] = None
                    self.count -= 1
                self.count += 1
                node = DoubleLikedList(key, value)
                self.insert_left(self.end, node)
                self.hash_node[key] = node
                self.hash_frequency[0] = node
                self.get(key)
            else:
                self.hash_node[key].val = value
                self.get(key)

    def delete_node(self, node):
        node.left.right, node.right.left = node.right, node.left

    def insert_left(self, anchor, node):
        anchor.left.right, node.left = node, anchor.left
        anchor.left, node.right = node, anchor

if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.put(4,1)
    print(cache.get(1))
    print(cache.get(2))
    # cache = LFUCache(0)
    # cache.put(0,0)
    # print(cache.get(0))

    # cache.put(1, 1)
    # cache.put(2, 2)
    # node = cache.end
    # # while node:
    # #     print(node.val)
    # #     node = node.left
    # print(cache.get(1))
    # cache.put(3, 3)
    # print(cache.get(2))
    # print(cache.get(3))
    # cache.put(4, 4)
    # print(cache.get(1))
    # print(cache.get(3))
    # print(cache.get(4))

