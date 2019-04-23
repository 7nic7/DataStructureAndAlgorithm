def longest_increasing_subsequence(sequence):
    """最长上升子序列 (时间复杂度 O(n^2)) 动态规划"""
    n = len(sequence)
    table = [1]*n
    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i]:
                table[i] = max([table[j]+1, table[i]])
    print(table)
    print(max(table))


def longest_increasing_subsequence_v2(sequence):
    """
    最长上升子序列 (时间复杂度 O(n log(n)))
        利用了二分查找
    """
    n = len(sequence)
    # 把subseq看作是栈
    subseq = [sequence[0]]
    for i in range(1, n):
        # 直接入栈
        if sequence[i] > subseq[-1]:
            subseq.append(sequence[i])
        else:
            # 二分查找出比subseq中比sequence[i]大的第一个数，并用sequence[i]作替换
            left, right = 0, len(subseq)-1
            while left < right:
                middle = (left+right)//2
                if subseq[middle] < sequence[i]:
                    left = middle + 1
                elif subseq[middle] > sequence[i]:
                    right = middle
                elif subseq[middle] == sequence[i]:
                    return
            subseq[left] = sequence[i]
    print(subseq)
    print(len(subseq))

if __name__ == '__main__':
    seq = [10, 9, 2, 5, 3, 7, 101, 18]
    longest_increasing_subsequence_v2(seq)


