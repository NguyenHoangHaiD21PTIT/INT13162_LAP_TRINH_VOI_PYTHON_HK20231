n = int(input())
firstEle = []
a = [] #Lưu các list đề cho
# Tạo tập các phần tử đầu tiên phân biệt
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
    if not b[0] in firstEle: firstEle.append(b[0])

#Mở rộng danh sách dựa trên key - phần tử đầu tiên
result = {}
for key in firstEle: result[key] = []
for x in a:
    key = x[0]
    result[key].extend(x[1:])  

# Tạo danh sách kết quả cuối cùng
output = []
for key in result:
    combined_tuple = [key] + result[key]
    output.append(tuple(combined_tuple))
print(output)