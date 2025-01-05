N, K = map(int, input().split())
student_scores = {}
for _ in range(N):
    name, score = input().split()
    score = int(score)
    student_scores[name] = score
a = sorted(student_scores.items(), key=lambda x: (-x[1], x[0]))
if N > 70 or K > 5 or N < 1 or K < 1 or K > N: print("INVALID INPUT")
else:
    for i in range(K): print(a[i][0], end = " ")