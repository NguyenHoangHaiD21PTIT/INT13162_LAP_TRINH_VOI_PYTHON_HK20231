def Try(n,a,b,c): #B la coc trung gian, C la coc dich
	if(n==1):
		print(a + " -> " + c)
		return
	#1. Chuyen n-1 dia be hon sang cot B
	Try(n-1, a, c, b)
	#2. Chuyen dia to nhat sang cot C
	Try(1,a,b,c)
	#3. Chuyen n-1 dia be chong tu B len C 
	Try(n-1,b,a,c)	
n = int(input())
Try(n, 'A', 'B', 'C')
