import math

from binary_serch_tree import TreeNode, search, insert, treeLevel



node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
print(root.value)
print(root.leftChild.leftChild)
print(root.rightChild.rightChild)

result = search(50, root)
print(result.value)


print(treeLevel(8))

# def countdown(number):
#     print(number)
#     if number<1:
#         return;
#     countdown(number-1)
    
# countdown(10)