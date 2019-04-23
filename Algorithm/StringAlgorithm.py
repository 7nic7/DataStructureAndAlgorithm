from pprint import pprint


def dynamic_string_match(main_str, sub_str):
    """动态回归， 找序列sub_str是否在main_str中出现（字符是连续的）"""
    mat = [[0 for _ in range(len(sub_str)+1)] for _ in range(len(main_str)+1)]
    max_L = 0
    for i in range(1, len(main_str)+1):
        for j in range(1, len(sub_str)+1):
            if main_str[i-1] == sub_str[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
                if mat[i][j] > max_L:
                    max_L = mat[i][j]
    if max_L == len(sub_str):
        print(True)
    else:
        print(False)
    pprint(mat)


def dynamic_substring_match(main_str, sub_str):
    """
    动态规划， 找子序列sub_str是否在main_str中出现（字符不是连续的）
        比如：main_str = 'atbicadn', sub_str = 'tian', 是匹配的，因为main_str中含有'tian'
    """
    mat = [[0 for _ in range(len(sub_str)+1)] for _ in range(len(main_str)+1)]
    location = [[None for _ in range(len(sub_str)+1)] for _ in range(len(main_str)+1)]
    max_L = 0
    for i in range(1, len(main_str)+1):
        for j in range(1, len(sub_str)+1):
            if main_str[i-1] == sub_str[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
                location[i][j] = 'ok'
            else:
                if mat[i-1][j] > mat[i][j-1]:
                    mat[i][j] = mat[i-1][j]
                    location[i][j] = 'up'
                else:
                    mat[i][j] = mat[i][j-1]
                    location[i][j] = 'left'
            if mat[i][j] > max_L:
                max_L = mat[i][j]
    if max_L == len(sub_str):
        print(True)
    else:
        print(False)
    pprint(location)
    pprint(mat)


class KMP(object):
    """
    KMP 算法 ：
        查找sub_str是否在main_str中存在
    """
    def __init__(self, main_str, sub_str):
        self.main_S = main_str
        self.sub_S = sub_str

    def gen_pnext(self):
        self.pnext = [0 for _ in range(len(self.sub_S))]
        i, j = 1, 0
        l = len(self.sub_S)
        while i < l:
            if self.sub_S[j] == self.sub_S[i]:
                self.pnext[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    self.pnext[i] = 0
                    i += 1
                else:
                    j = self.pnext[j-1]
        print(self.pnext)

    def kmp_algorithm(self):
        i, j = 0, 0
        while i < len(self.main_S):
            if self.main_S[i] == self.sub_S[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = self.pnext[j-1]
            if j == len(self.sub_S):
                print(True)
                return
        print(False)


def manacher(string):
    """计算最长的回文序列长度"""
    # 将字符串长度固定为奇数， 需要做一些变化
    string_odd = ''.join(['$' + i for i in string]) + '$'
    # 构造P， P可以存储(回文长度+1), 这也是manacher方法的核心部分， 利用到了对称信息
    P = [1]*len(string_odd)
    id_ = 0
    mx = P[id_]
    for i in range(1, len(string_odd)-1):
        if mx > i:
            P[i] = min([P[id_-(i-id_)], mx-i+1])
        # 暴力搜索mx右侧
        while P[i] + i < len(string_odd) and i - P[i] >= 0 and string_odd[P[i]+i] == string_odd[i-P[i]]:
            P[i] += 1
        # 更新mx和id_
        if P[i]+i-1 > mx:
            mx = P[i]+i-1
            id_ = i
    if max(P) == 1:
        print(-1)
    else:
        print(max(P)-1)
    print(P)
if __name__ == '__main__':
    # mainS = 'dasatian'
    # subS = 'tian'
    # dynamic_string_match(mainS, subS)
    # mainS = 'mtsidawn'
    # subS = 'tian'
    # mainS = 'dasdwe'
    # subS = 'ytry'
    # dynamic_substring_match(mainS, subS)
    # mainS = 'akaaadabjh'
    # subS = 'aaa'
    # subS = 'aabaabaaa'
    # kmp = KMP(mainS, subS)
    # kmp.gen_pnext()
    # kmp.kmp_algorithm()
    manacher('abaa')



