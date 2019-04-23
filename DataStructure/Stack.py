class Stack(object):
    def __init__(self):
        """用顺序表作为node，也可以用链表"""
        self.__tail = []

    def push(self, item):
        """压栈"""
        self.__tail.append(item)

    def pop(self):
        """弹栈"""
        return self.__tail.pop()

    def is_empty(self):
        """判断栈是否为空"""
        return self.__tail == []

    def size(self):
        """栈中有多少个元素"""
        return len(self.__tail)

if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    print(s.size())
    s.push(1)
    print(s.is_empty())
    s.push(2)
    s.push(3)
    print(s.size())

    print(s.pop())
    print(s.pop())
    print(s.pop())

