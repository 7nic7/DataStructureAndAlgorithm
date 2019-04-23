class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class CycleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node
        # 与单向链表不一样的地方
        if node:
            self.__head.next = node

    def is_empty(self):
        """
        判断链表是否为空
        """
        return self.__head is None

    def length(self):
        """
        计算链表的长度
        """
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def add(self, elem):
        """
        在链表头增加节点
        """
        if self.is_empty():
            self.append(elem)
        else:
            node = Node(elem)
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head = node

    def travel(self):
        """
        遍历所有节点
        """
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def append(self, elem):
        """
        在链表尾增加节点
        """
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, elem):
        """
        在pos的位置插入节点
        pos起始值是0
        """
        node = Node(elem)
        if pos == 0:
            self.add(elem)
        elif pos >= self.length():
            self.append(node)
        else:
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, elem):
        """查找元素是否在链表中"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == elem:
                return True
            cur = cur.next
        if cur.elem == elem:
            return True
        return False

    def remove(self, elem):
        """删除链表中第一个出现elem的元素"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            # 判断是否头节点已经是elem了
            if self.__head.elem == elem:
                rear = self.__head
                while rear.next != self.__head:
                    cur = cur.next
                node = cur.next
                self.__head = node
                rear.next = node
            else:
                if cur.next.elem == elem:
                    cur.next = cur.next.next
                    break
            cur = cur.next

if __name__ == '__main__':
    cll = CycleLinkedList()
    print(cll.is_empty())
    cll.remove(1)
    cll.append(1)
    print(cll.is_empty())

    cll.append(2)
    cll.append(3)
    cll.travel()
    cll.remove(3)
    cll.travel()

    cll.add(100)
    print(cll.length())
    cll.travel()

    cll.insert(2, 7)
    cll.travel()

    print(cll.search(2))
    print(cll.search(77))

    cll.append(2)
    cll.travel()
    cll.remove(2)
    cll.travel()
    cll.remove(2)
    cll.travel()

    print(cll.search(7))
    print(cll.search(8))
