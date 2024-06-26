from math import *
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    gcd_cost = {0: 0} #key là GCD, value là chi phí tối thiểu để đạt GCD đó
    
    # Duyệt qua từng thẻ
    for i in range(n):
        #Mỗi thẻ ta sẽ thử thêm vào các tập thẻ hiện có
        current_costs = list(gcd_cost.items())
        for g, cost in current_costs:
            new_g = gcd(g, l[i])
            new_cost = cost + c[i]
            if new_g not in gcd_cost or new_cost < gcd_cost[new_g]: gcd_cost[new_g] = new_cost
            print(gcd_cost)
    
    if 1 in gcd_cost: print(gcd_cost[1])
    else: print(-1)
