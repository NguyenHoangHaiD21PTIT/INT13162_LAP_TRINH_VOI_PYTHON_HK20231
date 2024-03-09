from math import *
from decimal import Decimal
class Point:
    def __init__(self, x, y):
        self.__x = x 
        self.__y = y   
    def distance(self, p):
        return "{:.4f}".format(sqrt((self.__x - p.__x) * (self.__x - p.__x) + (self.__y - p.__y) * (self.__y - p.__y))) 
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
