


class BinaryTree:
    """建立搜索二叉树"""

    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None
        if type(num) == list:
            self.num = num[0]
            for n in num[1:]:
                self.insert(n)
        else:
            self.num = num

    def insert(self, num):
        """对搜索二叉树插入数据"""
        bt = self
        while True:
            if num <= bt.num:
                if bt.left == None:
                    bt.left = BinaryTree(num)
                    break
                else:
                    bt = bt.left
            else:
                if bt.right == None:
                    bt.right = BinaryTree(num)
                    break
                else:
                    bt = bt.right


def front_recursion(root):
    """利用递归实现树的前序遍历"""

    if root is None:
        return

    print(root.num)
    front_recursion(root.left)
    front_recursion(root.right)


def middle_recursion(root):
    """利用递归实现树的中序遍历"""

    if root is None:
        return

    middle_recursion(root.left)
    print(root.num)
    middle_recursion(root.right)

def back_recursion(root):
    """利用递归实现树的后序遍历"""

    if root is None:
        return

    back_recursion(root.left)
    back_recursion(root.right)
    print(root.num)


def front_stack(root):
    """利用堆栈实现树的前序遍历"""

    if root is None:
        return

    stack = []
    node = root
    while node or stack:
        # 从根节点开始，一直找它的左子树
        while node:
            print(node.num)
            stack.append(node)
            node = node.left
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = stack.pop()
        # 开始查看它的右子树
        node = node.right



def middle_stack(root):
    """利用堆栈实现树的中序遍历"""

    if root is None:
        return

    stack = []
    node = root
    while node or stack:
        # 从根节点开始，一直找它的左子树
        while node:
            stack.append(node)
            node = node.left
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = stack.pop()
        print(node.num)
        # 开始查看它的右子树
        node = node.right



def back_stack(root):
    """利用堆栈实现树的后序遍历"""

    if root is None:
        return

    stack1 = []
    stack2 = []
    node = root
    stack1.append(node)
    # 这个while循环的功能是找出后序遍历的逆序，存在stack2里面
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    # 将stack2中的元素出栈，即为后序遍历次序
    while stack2:
        print(stack2.pop().num)


def level_queue(root):
    """利用队列实现树的层次遍历"""

    if root is None:
        return

    queue = []
    node = root
    queue.append(node)
    while queue:
        node = queue.pop(0)
        print(node.num)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    # 先输入结点总数n
    n = eval(input())

    # 输入n个结点，并加入列表
    num = []
    for i in range(n):
        num.append(eval(input()))
    bt = BinaryTree(num)

    print('队列实现层次遍历:')
    level_queue(bt)
    print('递归实现前序遍历:')
    front_recursion(bt)
    print('递归实现中序遍历:')
    middle_recursion(bt)
    print('递归实现后序遍历:')
    back_recursion(bt)
    print('堆栈实现前序遍历:')
    front_stack(bt)
    print('堆栈实现中序遍历:')
    middle_stack(bt)
    print('堆栈实现后序遍历:')
    back_stack(bt)
