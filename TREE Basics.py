import sys
class NewNode:
    def __init__(self, data):
        self.key = data
        self.right = None
        self.left = None
        self.parent = None
        
    def insert(self, root, key):
        if root==None:
            return
        elif root.key < key:
            if root.right ==None:
                root.right = NewNode(key)
                root.right.parent = root
            else:
                self.insert(root.right, key)
        elif root.key > key:
            if root.left ==None:
                root.left = NewNode(key)
                root.left.parent = root
            else:
                self.insert(root.left, key)
        elif root.key == key:
            print('Inserted node alredy available')
            return
            
                
    def delete(self, root, val_to_delete):
        previous_node = None
        #print('Value to delete from tree: ',val_to_delete 

        if val_to_delete > root.key:
            print('traverse right subtree')
            if root.right is not None:
                self.delete(root.right, val_to_delete)
        if val_to_delete < root.key:
            print('traverse left subtree')
            if root.left is not None:
                self.delete(root.left, val_to_delete)

        if root.key == val_to_delete:
            previous_node = root.parent
            if root.key > previous_node.key:
                previous_node.right =None
                print('Deleted Node')
                return
            if root.key < previous_node.key:
                previous_node.left =None
                print('Deleted Node')
                return
                
    def level_order(self, root, lst):
        Flag = True
        lst = lst[1:]
        #print('Length of lst before insertion :', len(lst))

        
        #Root Execution
        print('Root : ',root.key)
        #print('Its child ', end=' ' )
        if root.left is not None:
            L = root.left
            #print(L.key, end =' ')
            lst.append(L)
            
        if root.right is not None:
            R = root.right
            #print(R.key)
            lst.append(R)
            
        #print('Above If condition', len(lst))
        if (root.left is None) and (root.right is None):
            if len(lst)== 0 :
                #print('Inside IF Block')
                sys.exit()
                Falg = False
                return Falg
        #print('After If condition', len(lst))

        #print('\nLength of list after new root insertion :', len(lst))

        for i in range(len(lst)):
            #print('Inside for loop, List is:')
            
            
            if (len(lst)==0) & (root.left is None) & (root.right is None) :
                #print('Condition executed')
                return  
            self.level_order(lst[0], lst)



    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight +1
            else:
                return rheight +1

    def LevelOrder(self, root):
        queue = []
        lst = []
        queue.append(root)
        while (len(queue)>0):
            node = queue.pop(0)
            print(node.key, end =' ')
            lst.append(node.key)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return lst

    def PreOrder(self, root):
        if root:
            print(root.key, end=' ')
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def PostOrder(self, root):
        lst = []
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.key, end=' ')

    def getLeafCount(self, node):
        if node is None:
            return
        if (node.right is None and node.left is None):
            return 1
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)
            
    def Delection(self, root):
        if root==None:
            return 
        
        self.Delection(root.left)
        self.Delection(root.right)
        print('Deleting the node', root.key)
        root=None

    def InOrder(self, root):
        if root:
            self.InOrder(root.left)
            print(root.key, end =' ')
            self.InOrder(root.right)

    def Minimum(self, root):
        current = root
        while(current.left):
            current = current.left
        print(current.key)

    def Maximum(self, root):
        current = root
        while(current.right):
            current= current.right
        print('Maximum Value in Binary Tree: ', current.key)
            

if __name__ =='__main__':
    root = NewNode(20)
    root.insert(root, 10)
    root.insert(root, 30)
    root.insert(root,8)
    root.insert(root,15)
    root.insert(root,100)
    #root.insert(root,14)
    #root.insert(root,9)
    #root.insert(root,989)
    root.insert(root,20)
    root.insert(root,25)
    #root.insert(root,3)
    root.display()
    #root.delete(root, int(input('Value to delete')))
    #root.display()
    print('Level Order Traversal: ')
    lst = root.LevelOrder(root)
    print('\n', lst)
    print('Size of BT : ',len(lst))
    print('\n Pre Order Traversal')
    root.PreOrder(root)
    print('\n Post Order Traversal')
    #print(root.PostOrder(root))
    print('\n In Order Traversal')
    root.InOrder(root)
    min=lst[0]
    for i in range(len(lst)):
        if min>lst[i]:
            min = lst[i]
    print('\nMinimum node in BT:', min)

    root.Minimum(root)
    root.Maximum(root)

    root.Delection(root)
    root.display()
    print('Leaf Node in BT :', root.getLeafCount(root))

    
        

    
    
    

        
        
        
    


