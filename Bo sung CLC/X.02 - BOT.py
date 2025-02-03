# Nhập dữ liệu
n = int(input())
a = list(map(int, input().split()))
#..
current_sum = 0
max_sum = -float('inf')  
start = 0
end = 0
temp_start = 0  # Dùng để lưu chỉ số bắt đầu của dãy con hiện tại

for i in range(n):
    current_sum += a[i]
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i
    if current_sum < 0:
        current_sum = 0
        temp_start = i + 1  # Chuyển chỉ số bắt đầu dãy con tới phần tử tiếp theo
print(start + 1, end + 1, max_sum)
