from Algorithm.树.创建树 import CreateTree,printTree
def change_left_right(root):
    if root.left:
        change_left_right(root.left)
    if root.right:
        change_left_right(root.right)
    root.left,root.right = root.right,root.left

if __name__ == "__main__":
    root = CreateTree([1,2,3,4,5,6,7])
    change_left_right(root)
    print(printTree(root))


