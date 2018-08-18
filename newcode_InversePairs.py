#思路：归并排序的思想
#先把序列分割成子序列，统计子序列中的逆序对，再统计子序列间的逆序对
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
    def InversePairs(self, data):
        r = data
        r1 = data[:]
        self.MergeSort2(r, r1, 0, len(r)-1,)
        return self.count % 1000000007

    def Merge(self, r, r1, s, m, t):  # 合并两个有序序列
        i = s
        j = m + 1
        while i <= m and j <= t:
            if r[i] < r[j]:
                r1[s] = r[i]
                i += 1
            else:
                r1[s] = r[j]
                #下面一行代码很关键：表示左序列中有几个元素大于右序列当前元素。
                self.count += m - i + 1
                j += 1
            s += 1
        while i <= m:
            r1[s] = r[i]
            i += 1
            s += 1
        while j <= t:
            r1[s] = r[j]
            j += 1
            s += 1


    def MergeSort2(self, r, r1, s, t):
        if s == t:
            r1[s] = r[s]
        else:
            m = (s + t) // 2
            self.MergeSort2(r, r1, s, m)
            self.MergeSort2(r, r1, m + 1, t)
            r1 = r[:]
            self.Merge(r1, r, s, m, t)
            r1 = r[:]


print(Solution().InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))

