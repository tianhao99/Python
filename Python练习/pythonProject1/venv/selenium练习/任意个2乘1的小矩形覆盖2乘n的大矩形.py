

class Solution:
    def RectCover(self,target) :
        if(target==0):
            return 0
        elif(target==1):
            return 1
        elif(target==2):
            return 2
        else:
            return self.RectCover(target-2)+self.RectCover(target-1)
s = Solution()
n = eval(input())
print(s.RectCover(n))