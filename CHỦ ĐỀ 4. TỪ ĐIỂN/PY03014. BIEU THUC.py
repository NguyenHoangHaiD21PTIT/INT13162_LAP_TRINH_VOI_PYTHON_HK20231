for _ in range(int(input())):
    s = input()
    st = []
    cnt = 1
    for x in s:
        if x == '(':
            st.append(cnt)
            print(cnt, end=" ")
            cnt += 1
        elif x == ')':  
            print(st[-1], end=" ")
            st.pop()
    print()
            