class Node:
    def __init__(self, now, left, right):
        self.now = now
        self.left = left
        self.right = right


def preorder(node):
    print(node.now, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])


def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.now, end="")
    if node.right != ".":
        inorder(tree[node.right])


def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.now, end="")


n = int(input())

tree = {}
for _ in range(n):
    now, left, right = input().split()
    tree[now] = Node(now, left, right)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])
