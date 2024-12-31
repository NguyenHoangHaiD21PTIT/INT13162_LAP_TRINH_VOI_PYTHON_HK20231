class Computation:
    def __init__(self, n): self.n = n
    def Factorial(self):
        tich = 1
        for i in range(1, self.n + 1): tich *= i
        return tich
    def Prime(self):
        if self.n < 2: return "NO"
        for i in range(2, int(self.n**0.5) + 1):
            if self.n % i == 0: return "NO"
        return "YES"
    def listDiv(self):
        a = []
        for i in range(1, self.n + 1):
            if self.n%i==0: a.append(str(i)) 
        return ",".join(a)

n = int(input())
comp = Computation(n)
print(comp.Factorial())
print(comp.Prime())
print(comp.listDiv())
        