def permutation(str_list, pos):
    """返回字符串的全排列（无重复字符），递归"""
    if pos == len(str_list):
        print(' '.join(str_list))
    for i in range(pos, len(str_list)):
        str_list[pos], str_list[i] = str_list[i], str_list[pos]
        permutation(str_list, pos+1)
        str_list[pos], str_list[i] = str_list[i], str_list[pos]


def permutation_v2(str_list, pos):
    """返回字符串的全排列 (字符串中有重复的字符)，递归"""
    if pos == len(str_list):
        print(' '.join(str_list))
    for i in range(pos, len(str_list)):
        # 判断str_list[i]是否在之前出现过
        flag = False
        for j in str_list[pos:i]:       # 注意：str_list是从pos开始的
            if str_list[i] == j:
                flag = True
        if flag:
            continue
        str_list[pos], str_list[i] = str_list[i], str_list[pos]
        permutation_v2(str_list, pos+1)
        str_list[pos], str_list[i] = str_list[i], str_list[pos]


def permutation_dict_order(str_list):
    """全排列，按照字典序的思想"""
    # 最小序 和 最大序
    min_list = sorted(str_list)
    max_list = min_list[::-1]
    print(''.join(min_list))
    while max_list != min_list:
        # 找比min_list大的数字中最小的那个
        for i in range(len(min_list)-2, -1, -1):
            j = len(min_list)-1
            is_find = False
            while j > i:
                # 找到了
                if min_list[j] > min_list[i]:
                    min_list[i], min_list[j] = min_list[j], min_list[i]
                    min_list[(i+1):] = min_list[(i+1):][::-1]
                    is_find = True
                    break
                else:
                    j -= 1
            if is_find:
                break
        print(''.join(min_list))

if __name__ == '__main__':
    # permutation_v2(['1', '2', '2'], 0)
    permutation_dict_order(['1', '1', '3'])