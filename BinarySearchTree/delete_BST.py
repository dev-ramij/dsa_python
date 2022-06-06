# There may be three case possible:
# 1. We need to delete the leaf node
# 2. The deleted node may have only one subtree left or right
# 3. The deleted node have two subtree left and right
# In first case we just assign none to its parent node
# In second case we just perform delete operation for the subtree
# In third case we need to find the lowest value from the right subtree 
# and replace the value with it and perform the delete operation for the lowest node

def deleteNode(root, X):
    # if root is none return root
    if root is None:
        return root
    if X < root.data:
        # Then left will be the deleted node
        # if its current left is deleted node then it will return None
        # thats how it is deleted
        root.left = deleteNode(root.left, X)
    elif X > root.data:
        # same as left
        root.right = deleteNode(root.right, X)
    else:
        if root.left is None:
            # if left is none there may be a right subtree so return the right node
            # if right node is not None then parent node will assign its value
            # if none then None will be assigned
            return root.right
        if root.right is None:
            return root.left
        # if both are not none then we need to find minValue from the right subtree
        # we should not do it for left subtree because then there might be some 
        # ambuity for its parent node may be lowest value can be assigned to the right
        root.data = minValue(root.right)
        # then delete the lowest node
        root.right = deleteNode(root.right, root.data)
    return root

# getting the min value 
# we go to the leftest node that will be our minvalue
# 1. check if there is any left child present or not
# if present then data will be the left child data and assign the root to its left child
# else this will be our minvalue just return its data
def minValue(root):
    data = root.data
    while root.left:
        data = root.left.data
        root = root.left
    return data