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

data = [3, 9, 20, None, None, 15, 7]
root = construct_tree(data)

def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

print(maxDepth(root))  # 输出: 3
