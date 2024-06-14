import math

def treeLevel(nodeCount):
    level = math.log2(nodeCount) 
    print(type(level))

    # return level # roughly
    return math.ceil(level)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right
        

def search(searchValue, node):
    # 기저 조건: 노드가 없거나
    # 찾고 있던 값이면
    if node is None or node.value == searchValue:
        return node
    
    # 찾고 있는 값이 현재 노드보다 작으면
    # 왼쪽 자식을 검색한다
    elif searchValue <node.value:
        return search(searchValue, node.leftChild)
    
    # 찾고 있는 값이 현재 노드보다 크면
    # 오른쪽 자식을 검색한다
    else: # searchValue > node.value
         search(searchValue,node.rightChild)

         
def insert(value, node):
    if value < node.value:
        # 왼쪽 자식이 없으면 왼쪽 자식으로서 값을 삽입한다
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
            
    elif value > node.value:
        # 오른쪽 자식이 없으면 오른쪽 자식으로서 값을 삽입한다
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)
            
