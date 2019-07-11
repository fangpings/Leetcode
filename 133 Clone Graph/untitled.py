class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        ret = Node(node.val, [])
        queue = [(node, ret)]
        visited = {node.val:ret}
        while queue:
            tmp, new = queue.pop(0)
            for node in tmp.neighbors:
                if node.val not in visited:
                    neighbor = Node(node.val, [])
                    new.neighbors.append(neighbor)
                    queue.append((node, neighbor))
                    visited[node.val] = neighbor
                else:
                    new.neighbors.append(visited[node.val])
        return ret

