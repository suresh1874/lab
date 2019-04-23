def multiply():
	a,b=input("Enter size of first matrix:")
	A=input("Enter first matrix:")
	c,d=input("Enter size of second matrix:")
	B=input("Enter second matrix:")
	if(b==c):
		C=[[0 for col in range(a)] for row in range(d)]
		for i in range(0,a):
			for j in range(0,d):
				for k in range(0,b):
					C[i][j]=C[i][j]+(A[i][k])*(B[k][j])
		print('Result:\n')
		print(C)
	else:
		print('Multiplication is not possible with given inputs')
	

multiply()
