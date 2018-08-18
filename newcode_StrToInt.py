# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if len(s) == 0:
            return 0
        number = ['0','1','2','3','4','5','6','7','8','9']
        res = 0
        if s[0] == '+':
            if len(s) == 1:
                return 0
            if s[1] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j > 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
        elif s[0] == '-':
            if len(s) == 1:
                return 0
            if s[1] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j > 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
            res = res * (-1)
        else:
            if s[0] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j >= 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
        return res

    def StrToInt2(self, s):
        if len(s) == 0:
            return 0
        number = ['0','1','2','3','4','5','6','7','8','9']
        res = 0
        i = 0
        j = len(s) - 1
        while j > 1:
            if s[j] not in number:
                return 0
            res = res + int(s[j]) * (10 ** i)
            i = i + 1
            j = j - 1

        if s[0] == '+':
            if len(s) == 1:
                return 0
            if s[1] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j > 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
        elif s[0] == '-':
            if len(s) == 1:
                return 0
            if s[1] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j > 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
            res = res * (-1)
        else:
            if s[0] == '0':
                return 0
            i = 0
            j = len(s) - 1
            while j >= 0:
                if s[j] not in number:
                    return 0
                res = res + int(s[j])*(10**i)
                i = i + 1
                j = j - 1
        return res


print(Solution().StrToInt("0"))






