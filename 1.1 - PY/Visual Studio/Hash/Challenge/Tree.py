class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_child = left
    self.right_child = right

#Driver code
if __name__ == "__main__":
  #Create root
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
