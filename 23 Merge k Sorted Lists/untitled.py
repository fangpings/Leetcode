class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_node(self):
        cur = self
        while cur != None:
            print(cur.val)
            cur = cur.next

class heap(object):
    def __init__(self, nums, small_func=lambda x, y: x < y):
        self.min_flag = -10000
        self.judge = self.decorate_func(small_func)
        self.initialize(nums)

    def is_empty(self):
        return not self.size

    def decorate_func(self, small_func):
        def function(x, y):
            if x == self.min_flag:
                return True
            elif y == self.min_flag:
                return False
            else:
                return small_func(x, y)
        return function

    def percolate_down(self, index):
        if index > self.size:
            return
        element = self.heap[index]
        i = index
        while i * 2 <= self.size:
            child = i * 2
            if child != self.size and self.judge(self.heap[child + 1], self.heap[child]):
                child += 1
            if self.judge(self.heap[child], element):
                self.heap[i] = self.heap[child]
            else:
                break
            i = child
        self.heap[i] = element

    def initialize(self, nums):
        self.heap = [self.min_flag] + nums
        self.size = len(nums)
        i = self.size // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def delete_min(self):
        if self.is_empty():
            return None
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return ret

    def insert(self, element):
        i = self.size + 1
        self.heap.append(element)
        while self.judge(element, self.heap[i//2]):
            self.heap[i] = self.heap[i // 2]
            i = i // 2
        self.heap[i] = element
        self.size += 1

def mergeKLists(lists):

    class heap(object):
        def __init__(self, nums, small_func=lambda x, y: x < y):
            self.min_flag = -10000
            self.judge = self.decorate_func(small_func)
            self.initialize(nums)

        def is_empty(self):
            return not self.size

        def decorate_func(self, small_func):
            def function(x, y):
                if x == self.min_flag:
                    return True
                elif y == self.min_flag:
                    return False
                else:
                    return small_func(x, y)
            return function

        def percolate_down(self, index):
            if index > self.size:
                return
            element = self.heap[index]
            i = index
            while i * 2 <= self.size:
                child = i * 2
                if child != self.size and self.judge(self.heap[child + 1], self.heap[child]):
                    child += 1
                if self.judge(self.heap[child], element):
                    self.heap[i] = self.heap[child]
                else:
                    break
                i = child
            self.heap[i] = element

        def initialize(self, nums):
            self.heap = [self.min_flag] + nums
            self.size = len(nums)
            i = self.size // 2
            while i > 0:
                self.percolate_down(i)
                i -= 1

        def delete_min(self):
            if self.is_empty():
                return None
            if self.size == 1:
                self.size -= 1
                return self.heap.pop()
            ret = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.size -= 1
            self.percolate_down(1)
            return ret

        def insert(self, element):
            i = self.size + 1
            self.heap.append(element)
            while self.judge(element, self.heap[i//2]):
                self.heap[i] = self.heap[i // 2]
                i = i // 2
            self.heap[i] = element
            self.size += 1

    h = heap([], lambda x, y: x.val < y.val)

    for node in lists:
        if node == []:
            continue
        h.insert(node)
    head = ListNode(0)
    cur = head
    while not h.is_empty():
        tmp = h.delete_min()
        cur.next = ListNode(tmp.val)
        if tmp.next:
            h.insert(tmp.next)
        cur = cur.next
    return head.next



if __name__ == '__main__':
    l1 = ListNode(0)
    cur = l1
    for i in range(1, 5):
        cur.next = ListNode(i)
        cur = cur.next
    # l1.print_node()
    l2 = ListNode(0)
    cur = l2
    for i in range(5, 10):
        cur.next = ListNode(i)
        cur = cur.next
    # l2.print_node()
    l3 = mergeKLists([[], []])
    print(l3)

    # h = heap([])
    # h.insert(2)
    # h.insert(3)
    # h.insert(4)
    # h.delete_min()
    # h.insert(3)
    # h.delete_min()
    # h.insert(4)
    # while not h.is_empty():
    #     print(h.delete_min())










