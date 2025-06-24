from base import construct_tree

tree = [4,2,6,1,3,5,7]
root = construct_tree(tree)

def preorder(root):
    result = []
    def helper(node):
        if not node:
            return
        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result

def inorder(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result

print(inorder(root))