from DataStructureAndAlgorithm.DataStructure.SingleLinkList import SingleLinkedList


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None    # 与单链表不一样的地方


class DoubleLinkedList(SingleLinkedList):
    """
    一般要注意几种特殊形式：
        1.链表为空
        2.链表中只有一个元素
        3.在链表的头部或者尾部进行操作的时候
    """
    def __init__(self):
        super(DoubleLinkedList, self).__init__()

    def append(self, elem):
        """在链表尾部插入元素"""
        node = Node(elem)
        if self.is_empty():
            self._SingleLinkedList__head = node
        else:
            cur = self._SingleLinkedList__head
            while cur.next:
                cur = cur.next
            cur.next = node
            cur.prev = cur

    def insert(self, pos, elem):
        """在链表pos处插入元素"""
        node = Node(elem)
        if pos == 0:
            self.add(elem)
        elif pos >= self.length():      # 如果所给的pos大于长度，那就直接append
            self.append(elem)
        else:
            cur = self._SingleLinkedList__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next = node
            node.next.prev = node

    def search(self, elem):
        """查找元素是否在链表中"""
        cur = self._SingleLinkedList__head
        while cur:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False

    def remove(self, elem):
        """删除链表中第一个与elem相等的元素"""
        cur = self._SingleLinkedList__head
        while cur:
            # 判断是否头节点已经是elem了
            if self._SingleLinkedList__head.elem == elem:
                self._SingleLinkedList__head = cur.next
                if cur.next:
                    cur.next.prev = None
                break
            else:
                if cur.next.elem == elem:
                    cur.next = cur.next.next
                    if cur.next:
                        cur.next.prev = cur
                    break
                else:
                    if not cur.next:
                        break
            cur = cur.next

if __name__ == '__main__':
    dll = DoubleLinkedList()
    print(dll.is_empty())
    dll.append(1)
    # dll.travel()
    # dll.remove(1)
    dll.travel()
    print(dll.is_empty())
    dll.append(2)
    print(dll.is_empty())
    dll.travel()

    dll.insert(0, 100)
    dll.travel()
    dll.add(200)
    dll.append(23)
    dll.travel()
    dll.insert(4, 300)
    dll.travel()
    dll.remove(300)
    dll.insert(2, 150)
    dll.travel()
    #
    # dll.remove(150)
    # dll.travel()
    #
    # print(dll.search(200))
    # print(dll.search(400))