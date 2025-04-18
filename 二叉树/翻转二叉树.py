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

root = [4,2,7,1,3,6,9]

def invert_tree(node):
    if node is None:
        return None
    # 交换左右子树
    node.left, node.right = node.right, node.left
    # 递归反转左右子树
    invert_tree(node.left)
    invert_tree(node.right)
    return node