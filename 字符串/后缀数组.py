#sa[i]表示排名为i的后缀的起始字符下标为sa[i]
def build_sa(s,n,m, c, sa, x, y):
    for i in range(0,n):
        x[i] = s[i]
        c[ord(x[i])] += 1
    for i in range(1,m):
        c[i] += c[i-1]
    for i in range(n-1, -1, -1):
        c[ord(x[i])] -= 1
        sa[c[ord(x[i])]] = i
    k = 1
    while k <= n:
        p = 0
        for i in range(n-k,n):
            y[p] = i
            p += 1
        for i in range(0,n):
            if sa[i] >= k:
                y[p] = sa[i] - k
                p += 1
        for i in range(0,m):
            c[i] = 0
        if k == 1:
            for i in range(0, n):
                c[ord(x[y[i]])] += 1
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[ord(x[y[i]])] -= 1
                sa[c[ord(x[y[i]])]] = y[i]
        else:
            for i in range(0, n):
                c[x[y[i]]] += 1     #当k大于1时，因为x中元素全为整数，不再是ascil码，所以不能在使用ord
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[x[y[i]]] -= 1
                sa[c[x[y[i]]]] = y[i]
        x,y = y,x
        p = 1
        x[sa[0]] = 0
        for i in range(1,n):
            if y[sa[i-1]] == y[sa[i]] and y[sa[i-1]+k] == y[sa[i]+k]:
                x[sa[i]] = p - 1
            else:
                x[sa[i]] = p
                p += 1
        if p >= n:
            break
        m = p
        k = k * 2
    return

def build_sa2(s,n,m, c, sa, x, y):
    for i in range(0,n):
        x[i] = s[i]
        c[ord(x[i])] += 1
    for i in range(1,m):
        c[i] += c[i-1]
    for i in range(n-1, -1, -1):
        c[ord(x[i])] -= 1
        sa[c[ord(x[i])]] = i

    k = 1
    p = 1
    while p < n:
        p = 0
        for i in range(n-k,n):
            y[p] = i
            p += 1
        for i in range(0,n):
            if sa[i] >= k:
                y[p] = sa[i] - k
                p += 1
        for i in range(0,m):
            c[i] = 0
        if k == 1:
            for i in range(0, n):
                c[ord(x[y[i]])] += 1
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[ord(x[y[i]])] -= 1
                sa[c[ord(x[y[i]])]] = y[i]
        else:
            for i in range(0, n):
                c[x[y[i]]] += 1     #当k大于1时，因为x中元素全为整数，不再是ascil码，所以不能在使用ord
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[x[y[i]]] -= 1
                sa[c[x[y[i]]]] = y[i]
        x,y = y,x
        p = 1
        x[sa[0]] = 0
        for i in range(1,n):
            if y[sa[i-1]] == y[sa[i]] and y[sa[i-1]+k] == y[sa[i]+k]:
                x[sa[i]] = p - 1
            else:
                x[sa[i]] = p
                p += 1
        k += 1
    return
def get_height(s, sa, n, rank, height):
    k = 0
    for i in range(0, n):
        rank[sa[i]] = i
    for i in range(0,n):
        k = k-1
        if k < 0:
            k = 0
        j = sa[rank[i]-1]
        while j+k < len(s) and s[i+k] == s[j+k]:
            k = k + 1
        height[rank[i]] = k

# def get_height2(s, sa, n, rank, height):
#     h = 0
#     for i in range(0, n):
#         rank[sa[i]] = i
#     for

def get_suffix(s):
    m = 128  # 128个ascil
    n = len(s)
    maxn = 1000  # 字符串的最大长度
    c = [0] * maxn
    sa = [0] * maxn
    rank = [0] * maxn
    height = [0]*maxn
    x = [0] * maxn
    y = [0] * maxn
    suffix = [""] * n
    build_sa2(s, n, m, c, sa, x, y)
    get_height(s, sa, n, rank, height)
    print(height)
    for i in range(0, n):
        suffix[i] = s[sa[i]:]  # suffix中存储的就是排序后的后缀数组
    return suffix






if __name__ == "__main__":
    s = "aabaaaab"
    suffix = get_suffix(s)
    print(suffix)

