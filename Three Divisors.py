class Solution:
    def isThree(self, n: int) -> bool:
        soma = 0
        for i in range(1, n+1):
            if n%i==0:
                soma+=1
        if soma == 3:
            return True
        else:
            return False
