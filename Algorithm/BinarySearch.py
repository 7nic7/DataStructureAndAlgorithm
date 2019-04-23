def binary_search(list_data, item):
    """
    二分查找——使用递归思想
    Parameters:
        list_data: 必须是个有序的列表
        item: 是目标值，查看该值是否在list_data中
    """
    n = len(list_data)
    if n > 0:
        mid = n // 2
        if list_data[mid] == item:
            return True
        elif list_data[mid] < item:
            return binary_search(list_data[mid+1:], item)
        elif list_data[mid] > item:
            return binary_search(list_data[:mid], item)
    return False


def binary_search_v2(list_data, item):
    """
    二分查找——非递归
    """
    start_, end_ = 0, len(list_data)-1
    mid = (start_ + end_) // 2
    while start_ <= end_:
        if list_data[mid] == item:
            return True
        elif list_data[mid] < item:
            start_ = mid + 1
            mid = (start_ + end_) // 2
        elif list_data[mid] > item:
            end_ = mid - 1
            mid = (start_ + end_) // 2
    return False


if __name__ == '__main__':
    alist = [1,4,7,9,10,15,17,40,50,55]
    print(binary_search(alist, 40))
    print(binary_search(alist, -2))

    print(binary_search_v2(alist, 40))
    print(binary_search_v2(alist, -2))
