class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        ret = []
        q = [root]
        while q:
            tmp = q.pop(0)
            if tmp:
                ret.append(tmp.val)
                q.append(tmp.left)
                q.append(tmp.right)
            else:
                ret.append(None)
        while ret[-1] == None:
            ret.pop()
        return ret
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = data.pop(0)
        if root == None:
            return None 
        root = TreeNode(root)
        nodes = [root]
        while data != []:
            left_val = data.pop(0)
            right_val = data.pop(0) if data != [] else None
            node = nodes.pop(0)
            if left_val != None:
                node.left = TreeNode(left_val)
                nodes.append(node.left)
            if right_val != None:
                node.right = TreeNode(right_val)
                nodes.append(node.right)
        return root

if __name__ == '__main__':
    c = Codec()
    print(c.serialize(c.deserialize([0,0,0,0,None,None,1,None,None,None,2])))