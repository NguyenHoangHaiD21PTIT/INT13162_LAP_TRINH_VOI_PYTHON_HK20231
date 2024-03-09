n = int(input())
a = list(map(int, input().split()))
st = []  # stack lưu các số mà không ghép cặp được thành tổng chẵn
for i in range(n):
    if len(st)==0:  # stack rỗng --> Phần tử đang xét hiện tại không có số để ghép cặp
        st.append(a[i])
    else:
        if (st[-1] + a[i]) % 2 == 0:  st.pop() # Đã có cặp
        else: st.append(a[i])
print(len(st))