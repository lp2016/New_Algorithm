import sys
sys.setrecursionlimit(1000000)
class swapsort:

    def bubblesort(self,data):
        exchang=len(data)-1
        bound=exchang
        while exchang:
            exchang=0
            for j in range(0, bound):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    exchang = j
                    bound=exchang

    def quicksort(self,start,end,data):
        if start >=end:
            return
        key = self.onesort(start, end, data)
        self.quicksort(start, key - 1, data)
        self.quicksort(key + 1, end, data)

    def onesort(self,start,end,data):
        i=start
        j=end
        key=data[start]
        while i<j:
            while i<j and data[j]>=key:
                j-=1
            if data[j]<key:
                data[i],data[j]=data[j],data[i]
                i+=1
            while i<j and data[i]<=key:
                i+=1
            if data[i]>key:
                data[i],data[j]=data[j],data[i]
                j-=1
        return i

tt=swapsort()
a=list(range(0,1997,2))
tt.quicksort(0,len(a)-1,a)





