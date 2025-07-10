# [0] 기본 정보
# 이진 트리를 입력받아 세 가지 순회에 대한 출력을 구한다.

# [1] 전위 순회 (Pre-Order)

# [2] 중위 순회 (In-Order)

# [3] 후위 순회 (Post-Order)

class Node:
    def __init__(self, root):
        self.root = root
        self.left = "."
        self.right = "."

    def pre_order(self):
        print(self.root, end = "")
        
        if self.left != ".":
            self.left.pre_order()

        if self.right != ".":
            self.right.pre_order()

    def in_order(self):
        if self.left != ".":
            self.left.in_order()
        
        print(self.root, end = "")
        
        if self.right != ".":
            self.right.in_order()
        
    def post_order(self):
        if self.left != ".":
            self.left.post_order()

        if self.right != ".":
            self.right.post_order()

        print(self.root, end = "")

# 입력
# 이진 트리의 노드 개수 N (1 <= N <= 26)
# N개의 줄에 걸쳐 각 노드와 왼쪽 자식, 오른쪽 자식이 주어진다.
# 단, 노드의 이름은 알파벳 대문자이고 항상 A가 루트 노드이다. 또한, 자식이 없으면 .으로 표현
N = int(input())
nodes = {}
for _ in range(N):
    root, left, right = input().split()
    if root not in nodes:
        nodes[root] = Node(root)

    if left != ".":
        nodes[left] = Node(left)
        nodes[root].left = nodes[left]

    if right != ".":
        nodes[right] = Node(right)
        nodes[root].right = nodes[right]

# 출력
root = nodes["A"]
# 전위 순회의 결과
root.pre_order()
print()
# 중위 순회의 결과
root.in_order()
print()
# 후위 순회의 결과
root.post_order()