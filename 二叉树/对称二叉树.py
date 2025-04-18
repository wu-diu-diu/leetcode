class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(data):
    if not data or data[0] is None:
        return None
    
    root = TreeNode(data[0])
    queue = [root]
    i = 1
    
    while i < len(data):
        current_node = queue.pop(0)
        
        # 处理左子节点
        if i < len(data) and data[i] is not None:
            left_node = TreeNode(data[i])
            current_node.left = left_node
            queue.append(left_node)
        i += 1
        
        # 处理右子节点
        if i < len(data) and data[i] is not None:
            right_node = TreeNode(data[i])
            current_node.right = right_node
            queue.append(right_node)
        i += 1
    
    return root

root_list = [1,2,2,3,4,4,3]
root = construct_tree(root_list)

def isSymmetric(root):
    def recur(L, R):
        # 当左右子树都为空时，表明同时到达了叶子节点，返回True
        if not L and not R: return True
        # 当左右子树有一个为空时，则不对称，返回false，若果都不为空，则判断值是否相等，不相等也返回false
        if not L or not R or L.val != R.val: return False

        return recur(L.left, R.right) and recur(L.right, R.left)
    # 当根节点为空时，返回true
    # 当根节点不为空时，判断左右子树是否对称，返回true或false
    return not root or recur(root.left, root.right)
