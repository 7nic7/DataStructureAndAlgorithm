def bubble(list_data):
    """
    冒泡排序
        时间复杂度 : O(n^2)
        稳定性 : 稳定
    """
    n = len(list_data)
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(i):
            if list_data[j] > list_data[j+1]:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
            else:
                count += 1
        if count == n-1:
            return list_data
    return list_data


def select(list_data):
    """
    选择排序
        时间复杂度 : O(n^2)
        稳定性 : 不稳定
    """
    n = len(list_data)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if list_data[min_index] > list_data[i]:
                min_index = i
        list_data[j], list_data[min_index] = list_data[min_index], list_data[j]
    return list_data


def insert(list_data):
    """
    插入排序
        时间复杂度 : O(n^2)
        稳定性 : 稳定
    """
    n = len(list_data)
    for i in range(1, n):
        while i > 0:
            if list_data[i] < list_data[i-1]:
                list_data[i], list_data[i-1] = list_data[i-1], list_data[i]
                i -= 1
            else:
                break
    return list_data


def quick(list_data):
    """
    快速排序
    """
    n = len(list_data)
    low, high = 0, n
    target = list_data[0]
    while low != high:
        if list_data[low] < target:
            low += 1
        else:
            if list_data[high] > target:
                high -= 1
            else:
                list_data[low], list_data[high] = list_data[high], list_data[low]
    


if __name__ == '__main__':
    li = [4,2,1,6,9,-2]
    # print(bubble(li))
    # print(select(li))
    print(insert(li))

    li2 = [1,2,3,4,5,6]
    # print(bubble(li2))
    # print(select(li2))
    print(insert(li2))

