class Queue(object):
    def __init__(self):
        """用顺序表作为node，也可以用链表"""
        self.__body = []

    def push(self, item):
        """入队"""
        self.__body.append(item)

    def pop(self):
        """出队"""
        return self.__body.pop(0)

    def is_empty(self):
        """判断栈是否为空"""
        return self.__body == []

    def size(self):
        """栈中有多少个元素"""
        return len(self.__body)

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    print(q.size())
    q.push(1)
    print(q.is_empty())
    q.push(2)
    q.push(3)
    print(q.size())

    print(q.pop())
    print(q.pop())
    print(q.pop())

