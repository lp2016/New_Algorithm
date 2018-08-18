from heapq import heappush,heappop
a = 1
heap = []                   #创建堆
heappush(heap,a)            #插入元素到堆
num = heappop(heap)         #弹出堆顶元素
num2 = heap[0]              #读取堆顶元素
