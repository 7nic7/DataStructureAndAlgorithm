import numpy as np
import matplotlib.pyplot as plt

class GA(object):
    """遗传算法——匹配字符串"""
    def __init__(self, pop_num, pop_len, iter_, cross_p, mutate_p):
        self.pop_num = pop_num      # 种群大小
        self.pop_len = pop_len      # 种群中一个个体的长度
        self.iter = iter_           # 迭代次数
        self.cross_p = cross_p      # 交叉概率
        self.mutate_p = mutate_p    # 变异概率

    def init_pop(self):
        """初始化种群"""
        self.pop = np.random.randint(0, 27, [self.pop_num, self.pop_len])

    def fitness(self, target):
        """计算适应度"""
        fit_values = []
        target = np.array(target)
        for i in range(self.pop_num):
            value = sum(target == self.pop[i])
            fit_values.append(value + 1e-4)
        return fit_values

    def selection(self, fit_values):
        """种群选择"""
        # 将适应度值小于0的变为0，为了下面计算概率
        fit_values = [0 if i < 0 else i for i in fit_values]
        # 计算概率
        fit_values = np.array(fit_values)
        p = fit_values / sum(fit_values)
        # 概率选择法
        # 注意：我原来用的是将适应度值小的直接给删掉，如下
        # self.pop = self.pop[p > np.random.rand(self.pop_num)]
        # 但是这样做是有问题的，最后得到的图显示，不能收敛，可能没有把好的给保留下来
        indices = np.random.choice(np.arange(self.pop_num), self.pop_num, True, p)
        self.pop = self.pop[indices]

    def crossover(self):
        """交叉运算"""
        rand = np.random.rand(len(self.pop))
        for i in range(len(self.pop)-1):
            if self.cross_p > rand[i]:
                # 选择相邻的个体进行交换运算
                cpoint = int(np.random.randint(1, self.pop_len, 1))
                temp1, temp2 = np.zeros_like(self.pop[i]), np.zeros_like(self.pop[i+1])
                temp1[:cpoint] = self.pop[i, :cpoint]
                temp1[cpoint:] = self.pop[i+1, cpoint:]
                temp2[:cpoint] = self.pop[i+1, :cpoint]
                temp2[cpoint:] = self.pop[i, cpoint:]

                self.pop[i], self.pop[i+1] = temp1, temp2

    def mutation(self):
        """变异运算"""
        rand = np.random.rand(len(self.pop))
        for i in range(len(self.pop)):
            if self.mutate_p > rand[i]:
                # 单点变异
                mpoint = np.random.randint(0, self.pop_len, 1)
                self.pop[i, mpoint] = np.random.randint(0, 27, 1)

    # def add_pop(self):
    #     """产生新个体使得种群数目不变"""
    #     add_num = self.pop_num - len(self.pop)
    #     self.pop = np.vstack((np.random.randint(0, 27, [add_num, self.pop_len]), self.pop))

    def main(self, target):
        # 初始化种群
        self.init_pop()
        max_ = 0
        self.max_list = []
        self.guess = []
        for i in range(self.iter):
            # 计算适应度函数
            fit_values = self.fitness(target)
            # 优胜劣汰（种群选择）
            self.selection(fit_values)
            # 交叉运算
            self.crossover()
            # 变异运算
            self.mutation()
            # # 为了确保种群的总数不发生变化，增添新的个体
            # self.add_pop()
            # 保存一下最好的结果和其相应的适应度值
            if max(fit_values) > max_:
                max_ = max(fit_values)
                self.max_list.append(max(fit_values))
                self.guess.append(self.pop[np.argmax(fit_values)])

def str2num(string):
    """将字母转化为数字，数字即为它在字母表的位置"""
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    letter = np.array(letter)
    nums = []
    for i in string:
        nums.extend(np.where(i == letter)[0])
    return nums


def num2str(nums):
    """将数字再转化为字符串"""
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    letter = np.array(letter)
    string = letter[nums]
    return ''.join(string)


if __name__ == '__main__':
    # 假设只知道字符串的长度，但是不知道字符串是什么
    t_str = 'hello world'
    t_len = len(t_str)
    t_num = str2num(t_str)
    print(t_num)
    # ans = num2str(t_num)
    # print(ans)
    ga = GA(300, t_len, 2000, 0.4, 0.01)
    ga.main(t_num)
    for i in ga.guess:
        print(num2str(i))
    plt.plot(ga.max_list)
    plt.show()

