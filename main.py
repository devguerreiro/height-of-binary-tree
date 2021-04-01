def height(root):
    if root is None:
        return -1
    
    height_left = height(root.left)
    height_right = height(root.right)
    
    if (height_left == -1 and height_right == -1) or height_left >= height_right:
        return height_left + 1
    
    return height_right + 1
