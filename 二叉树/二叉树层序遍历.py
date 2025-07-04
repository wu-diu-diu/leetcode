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

list = [1,2,3,4,None, None, 5]
root = construct_tree(list)

## 使用队列来进行层序遍历
def level_order(root):
    if not root: return []
    queue = [root]
    ans = []
    while queue:
        val = []
        ## 取出当前层的元素个数
        length = len(queue)
        for _ in range(length):  # 用for循环来遍历当前层的节点
            ## 根据当前层的元素个数，依次取出当前层的所有节点
            node = queue.pop(0)
            val.append(node.val)
            ## 将下一层的所有节点按照左至右的顺序添加到队列中
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        ans.append(val)
    return ans  

print(level_order(root))