class Student:
    def __init__(self, name, s):
        self.name = name.strip()
        tmp = list(map(int, s.strip().split()))
        self.cor = tmp[0]
        self.sub = tmp[1]
    def __str__(self):
        return f'{self.name} {self.cor} {self.sub}'

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        tmp = Student(input(), input())
        a.append(tmp)
    a.sort(key = lambda x: (-x.cor, x.sub, x.name))
    for x in a: print(x)