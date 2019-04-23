class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        """
        return self.__head == None

    def length(self):
        """
        计算链表的长度
        """
        count = 0
        cur = self.__head
        while cur:
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
            self.__head = node

    def travel(self):
        """
        遍历所有节点
        """
        cur = self.__head
        while cur:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def append(self, elem):
        """
        在链表尾增加节点
        """
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        """
        在pos的位置插入节点
        pos起始值是0
        """
        node = Node(elem)
        if pos == 0:
            self.add(elem)
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
        cur = self.__head
        while cur:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False

    def remove(self, elem):
        """删除链表中第一个出现elem的元素"""
        cur = self.__head
        while cur:
            # 判断是否头节点已经是elem了
            if self.__head.elem == elem:
                self.__head = cur.next
            else:
                if cur.next.elem == elem:
                    cur.next = cur.next.next
                    break
                else:
                    if not cur.next:
                        break
            cur = cur.next

if __name__ == '__main__':
    sll = SingleLinkedList()
    print(sll.is_empty())
    sll.remove(1)
    sll.append(1)
    print(sll.is_empty())

    sll.append(2)
    sll.append(3)
    sll.travel()
    sll.remove(3)
    sll.travel()

    sll.travel()
    sll.add(100)
    print(sll.length())
    sll.travel()

    sll.insert(2, 7)
    sll.travel()

    print(sll.search(2))
    print(sll.search(77))

    sll.append(2)
    sll.travel()
    sll.remove(2)
    sll.travel()

    print(sll.search(7))
    print(sll.search(8))
