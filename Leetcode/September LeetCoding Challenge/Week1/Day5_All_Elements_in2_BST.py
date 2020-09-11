'''
Question: Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
      2               1
  1       4       0       3
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
'''
class Solution:
    # To traverse the Nodes of each tree   
    def traverse(self,root):
        self.temp=[]
        # Traversing the Nodes
        def order(root):
            if not root:
                return
            order(root.left)
            self.temp.append(root.val)
            order(root.right)
            
        order(root)
        return self.temp
        
    # Merging and Sorting the Values of 2 array
    # and return the result list
    def mergeTwoSortedArray(self,node1_val,node2_val):
        result = node1_val + node2_val
        result.sort()
        
        return result
        
    # Will fetch get the 2 BST
    # Calls the traverse()
    # Finally returns the List after mergeTwoSortedArray()
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root_list1 = self.traverse(root1)
        root_list2 = self.traverse(root2)
        
        return self.mergeTwoSortedArray(root_list1,root_list2)    
