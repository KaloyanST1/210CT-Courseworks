class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def Inorder(tree):
     
    # Set current to root of binary tree
    current = tree
    s = [] 
    done = 0
     
    while(not done):        
        # Reach the left most Node of the current Node
        if current is not None:
            s.append(current)
            current = current.left 
        else:
            if(len(s) >0 ):
                current = s.pop()
                print (current.value)
                current = current.right 
            else:
                done = 1
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  Inorder(t)
