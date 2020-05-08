#method return true if 
# n is Happy number 
class Solution:
    def isHappy(self, n: int)->bool: 
        sumSet = set()
        while(n not in sumSet):
            sumSet.add(n)
            sum_n = 0
            temp = n
            while(temp != 0):
                sum_n = sum_n + (temp % 10)**2
                temp = temp // 10
            if(sum_n == 1):
                return(True)
            n = sum_n
        return False
