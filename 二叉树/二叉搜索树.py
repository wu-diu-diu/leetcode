from base import construct_tree

root_list_0 = [3, 2, None, 1]
root_list_1 = [5, 3, 5, None, 4]
root_list_2 = [4, 2, 6, 1, 3, 5, 7]
root_list_3 = [4, 5, 6]
root = construct_tree(root_list_2)

def MyisSearch(root):
    if not root:
        return True
    left = root.left
    right = root.right
    if not left and not right:
        return True
    if left and not right and left.val < root.val:
        return MyisSearch(left)
    elif right and not left and root.val < right.val:
        return MyisSearch(right)
    elif right and left and left.val < root.val < right.val:
        return MyisSearch(left) and MyisSearch(right)
    else:
        return False

# 递归边界法
# 在递归中缩小边界，因为二叉搜索树的每一个zi'shu
def isSearch(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (isSearch(root.left, min_val, root.val) and 
            isSearch(root.right, root.val, max_val))

# 中序遍历法
# 根据中序遍历的性质，其就是先左子树，后根节点，最后右子树的顺序取出二叉树的元素
# 则如果取出来后的元素是递增的，那么必定满足二叉搜索树的定义
def isSearch_inorder(root):
    result = []
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    result.append(inorder(root))
    result = result[0]
    return all([result[i] < result[i+1] for i in range(len(result) - 1)])

print(isSearch_inorder(root))
