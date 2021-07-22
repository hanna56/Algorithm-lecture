# 이진 트리의 넓이 우선 순회
class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        arr_queue = ArrayQueue()
        if self.root:
            arr_queue.enqueue(self.root)
            while arr_queue.isEmpty() != True:
                pop_t = arr_queue.dequeue()
                traversal.append(pop_t.data)
                if pop_t.left:
                    arr_queue.enqueue(pop_t.left)
                if pop_t.right:
                    arr_queue.enqueue(pop_t.right)
        return traversal
        


def solution(x):
    return 0
